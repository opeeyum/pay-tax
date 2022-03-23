from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, UpdateUserForm
from .models import CustomUser

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

def edit_user(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UpdateUserForm(instance=user)

    return render(request, 'users/edit_user.html', {"form":form,})
    
