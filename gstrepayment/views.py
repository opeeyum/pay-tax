from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now

from users.models import CustomUser

from .models import Entry, OtherTaxes
from .forms import SaleTaxForm, SaleTaxFormPayer, OtherTaxForm, OtherTaxFormPayer

# Create your views here.
def home_page(request):
    context = {"q": None}
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.user_type == 'TA':
            entry_list = Entry.objects.all()
            other_tax_list = OtherTaxes.objects.all()
        else:
            entry_list = Entry.objects.filter(seller__id = request.user.id).all()
            other_tax_list = OtherTaxes.objects.filter(tax_payer__id = request.user.id).all()
            
        context["other_entries"] = other_tax_list
        context["entries"] = entry_list
        
    return render(request, 'gstrepayment/home.html', context)

@login_required
def add_entry(request):    
    if request.method == 'POST':
        form = SaleTaxFormPayer(request.POST)
        if form.is_valid():
            buyer = request.POST["buyer"]
            sale_item = request.POST["sale_item"]
            amount = request.POST["amount"]
            gst_percent = request.POST["gst_percent"]

            obj = Entry.objects.create(
                seller = request.user,
                buyer = buyer,
                sale_item = sale_item,
                amount = amount,
                is_paid = False,
                gst_percent = gst_percent,
            )
            obj.save()
            return redirect('home')
    
    else:
        form = SaleTaxFormPayer()
    context = {"form": form,}
    return render(request, 'gstrepayment/add_entry.html', context)

@login_required
def edit_entry(request, pk):
    obj = Entry.objects.get(pk=pk)
    page_type = "Update"

    # Form for Accountant and Admin
    if request.user.is_superuser or request.user.user_type == 'TA':
        if request.method == 'POST':
            form = SaleTaxForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('home')    
        else:
            form = SaleTaxForm(instance=obj)
    
    # Form for tax payer
    else:
        if request.method == 'POST':
            form = SaleTaxFormPayer(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('home')    
        else:
            form = SaleTaxFormPayer(instance=obj)

    context = {
        "form": form,
        "page_type": page_type}
    return render(request, 'gstrepayment/add_entry.html', context)

@login_required
def delete_entry(request, pk):
    obj = Entry.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    else:        
        return render(request, "gstrepayment/delete_entry.html", {"obj":obj,})

#=========== Tax payment sales ==============
@login_required
def pay_sales_tax(request, pk):
    obj = Entry.objects.get(pk=pk)
    
    # If anyone other than tax payer tries to pay tax on sales
    if obj.seller.id != request.user.id:
        messages.error(request, "Only Tax Payer can Pay!")
        return redirect('home')

    amount = obj.cgst + obj.igst + obj.sgst
    context = {
        "obj": obj,
        "amount": amount,
    }
    if request.method == "POST":
        obj.is_paid = True
        obj.is_due = False
        obj.save()
        return redirect('home')
    
    else:
        return render(request, 'gstrepayment/make_payment.html', context)

#========================== Other Taxes ============
@login_required
def add_other_tax(request):    
    if request.method == 'POST':
        form = OtherTaxForm(request.POST)
        if form.is_valid():
            tax_payer = CustomUser.objects.get(pk = request.POST["tax_payer"])            
            amount = request.POST["amount"]
            due_date = request.POST["due_date"]

            obj = OtherTaxes.objects.create(
                accountant = request.user,
                tax_payer = tax_payer,
                amount = amount,
                is_paid = False,
                due_date = due_date,
            )
            obj.save()
            return redirect('home')    
    else:
        form = OtherTaxForm()
    context = {"form": form,}
    return render(request, 'gstrepayment/add_entry.html', context)

@login_required
def edit_other_tax(request, pk):
    obj = OtherTaxes.objects.get(pk=pk)
    page_type = "Update"

    # Form for Accountant
    if request.user.is_superuser or request.user.user_type == 'TA':
        if request.method == 'POST':
            form = OtherTaxForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('home')    
        else:
            form = OtherTaxForm(instance=obj)
    else: 
        if request.method == 'POST':
            form = OtherTaxFormPayer(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('home')    
        else:
            form = OtherTaxFormPayer(instance=obj)

    context = {
        "form": form,
        "page_type": page_type,
        }
    return render(request, 'gstrepayment/add_entry.html', context)

@login_required
def delete_other_tax(request, pk):
    obj = OtherTaxes.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    else:        
        return render(request, "gstrepayment/delete_entry.html", {"obj":obj,})

#=========== Tax payment Other taxes ==============
@login_required
def pay_other_tax(request, pk):
    obj = OtherTaxes.objects.get(pk=pk)
    
    # If anyone other than tax payer tries to pay tax
    if obj.tax_payer.id != request.user.id:
        messages.error(request, "Only Tax Payer can Pay!")
        return redirect('home')

    context = {
        "obj": obj,
        "amount": obj.amount,
    }
    if request.method == "POST":
        obj.is_paid = True
        obj.is_due = False
        obj.save()
        return redirect('home')
    
    else:
        return render(request, 'gstrepayment/make_payment.html', context)

#===================== Filter entries + Other taxes =================
@login_required
def filter_entry(request):
    q = request.GET.get('q')

    # if Request made by admin or Tax Accountant
    if request.user.is_superuser or request.user.user_type == 'TA':
        if q == "is_paid":
            entry_list = Entry.objects.filter(is_paid=True).all()
            other_tax_list = OtherTaxes.objects.filter(is_paid=True).all()
        elif q == "is_due":
            today_date = now().replace(hour=0, minute=0, second=0, microsecond=0)
            entry_list = Entry.objects.filter(
                is_paid=False, 
                due_date__lte = today_date,
                ).all()
            other_tax_list = OtherTaxes.objects.filter(
                is_paid=False, 
                due_date__lte = today_date,
                ).all()
    
    # If request made by tax payer
    else:
        if q == "is_paid":
            entry_list = Entry.objects.filter(
                seller__id = request.user.id, 
                is_paid=True, 
                ).all()
            other_tax_list = OtherTaxes.objects.filter(
                tax_payer__id = request.user.id, 
                is_paid=True,
                ).all()
        elif q == "is_due":
            today_date = now().replace(hour=0, minute=0, second=0, microsecond=0)
            entry_list = Entry.objects.filter(
                seller__id = request.user.id, 
                is_paid=False,
                due_date__lte = today_date,
                ).all()
            other_tax_list = OtherTaxes.objects.filter(
                tax_payer__id = request.user.id,
                is_paid=False,
                due_date__lte = today_date,
                ).all()
        
    context = {
        "entries": entry_list, 
        "other_entries": other_tax_list,
        "q":q,
        }
    return render(request, 'gstrepayment/home.html', context)

