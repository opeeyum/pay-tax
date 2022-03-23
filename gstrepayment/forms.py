from django import forms
from .models import Entry, OtherTaxes

class SaleTaxForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['sale_item', 'buyer', 'amount', 'gst_percent', "due_date"]

class SaleTaxFormPayer(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['sale_item', 'buyer', 'amount', 'gst_percent']

class OtherTaxForm(forms.ModelForm):
    class Meta: 
        model = OtherTaxes
        fields = ['tax_name', 'tax_payer', 'amount', "due_date"]

class OtherTaxFormPayer(forms.ModelForm):
    class Meta: 
        model = OtherTaxes
        fields = ['tax_name', 'tax_payer', 'amount']
