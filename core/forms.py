from django import forms

class Register_form(forms.Form):
    Username = forms.CharField(label="username",min_length=3,max_length=30,required=True)
    Email = forms.EmailField(label="email",required=True)
    Password = forms.CharField(label="password",min_length=8,required=True)
    ConfirmPassword = forms.CharField(label="password_confirm",required=True)
