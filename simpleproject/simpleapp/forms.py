from django import forms

class RegisterForm(forms.Form):
    firstName   = forms.CharField(required = True)
    lastName    = forms.CharField()
    email       = forms.CharField(required = True)
    password    = forms.CharField(required = True)
    confirm_password = forms.CharField(required = True)
