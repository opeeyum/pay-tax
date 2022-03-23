from tkinter import CURRENT
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('user_type', 'gst_num')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'gst_num']