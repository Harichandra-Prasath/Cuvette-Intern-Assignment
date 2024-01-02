from django import forms

class Register_form(forms.Form):
    Username = forms.CharField(label="Username",min_length=3,max_length=30,required=True)
    Email = forms.EmailField(label="Email",required=True)
    Password = forms.CharField(label="Password",min_length=8,required=True)
    ConfirmPassword = forms.CharField(label="Confirm Password",required=True)

class Login_form(forms.Form):
    IdField = forms.CharField(label="Username or Email",required=True)
    Password = forms.CharField(label="Password",required=True)
