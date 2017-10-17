from django.forms import ModelForm
from django import forms
from .models import User


class UserSignupForm(forms.Form):

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    email = forms.EmailField()
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=64, widget=forms.PasswordInput)