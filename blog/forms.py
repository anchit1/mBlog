from django.forms import ModelForm
from django import forms

class UserSignupForm(forms.Form):

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    email = forms.CharField(max_length=75)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=64, widget=forms.PasswordInput)

class UserSignupForm2(forms.Form):

    city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    country = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'autocomplete': 'off'}))


class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=16)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
