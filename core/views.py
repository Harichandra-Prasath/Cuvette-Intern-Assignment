from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
# Create your views here.


# Register View
def register(request):
    if request.method=="POST":
        form = Register_form(request.POST)

        # Form validation 
        if form.is_valid():
            username = form.cleaned_data["Username"]
            email = form.cleaned_data["Email"]
            
            # Password Matching check
            if form.cleaned_data["Password"]!=form.cleaned_data["ConfirmPassword"]:
                return render(request,"core/register.html",{
                    "message":"Passwords did not match.Try again"     # sending error context
                })            
            password = form.cleaned_data["Password"] # password after check

            # User Creation
            try:
                user = User.objects.create_user(username=username,password=password,email=email)

                # Above create_user function calls make_password() on itself for hashing 
                # It is same as using set_password() method on the user for password hashing
                user.save()
            except IntegrityError:             
                return render(request,"core/register.hmtl",{
                    "message":"Username already Exists.Try again"
                })
                # we are using integrity error to catch the duplication in db
            return HttpResponseRedirect(reverse("login"))
    else:
        form = Register_form()
        return render(request,"core/register.html",{"form":form})
                




# login view
def login_view(request):
    if request.method=="POST":
        pass


    return render(request,"core/login.html")