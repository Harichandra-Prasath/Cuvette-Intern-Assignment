from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect,JsonResponse
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


# Register View
def register_view(request):
    if request.method=="POST":
        form = Register_form(request.POST)

        # Form validation 
        if form.is_valid():
            username = form.cleaned_data["Username"]
            email = form.cleaned_data["Email"]
            
            # Password Matching check
            if form.cleaned_data["Password"]!=form.cleaned_data["ConfirmPassword"]:
                return render(request,"core/register.html",{
                    "message":"Passwords did not match.Try again",     # sending error context
                    "form":form
                })            
            password = form.cleaned_data["Password"] # password after check

            # User Creation
            try:
                user = User.objects.create_user(username=username,password=password,email=email)

                # Above create_user function calls make_password() on itself for hashing 
                # It is same as using set_password() method on the user for password hashing
                user.save()
            except IntegrityError:
                if User.objects.filter(username=username).exists():
                    return render(request,"core/register.html",{
                        "message":"Username already Exists.Try again",
                        "form":form
                    })
                elif User.objects.filter(email=email).exists():
                    return render(request,"core/register.html",{
                        "message":"Already an User with given email account.Try again",
                        "form":form
                    })                
                # we are using integrity error to catch the duplication in db
            return HttpResponseRedirect(reverse("login"))
    else:
        form = Register_form()
        return render(request,"core/register.html",{"form":form})
                




# login view
def login_view(request):
    if request.method=="POST":
        form = Login_form(request.POST)

        if form.is_valid():
            Id_field = form.cleaned_data["IdField"] # Can be either username or email
            password = form.cleaned_data["Password"]


            # checking by exists function to get whether user entered username or email
            is_username =  User.objects.filter(username=Id_field).exists() 
            is_email = User.objects.filter(email=Id_field).exists()       

            # Individual cases for email and username
            if is_username:
                user = authenticate(request,username=Id_field,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    return render(request, "core/login.html", {
                        "message": "Invalid Credentials",
                        "form":form
                    })
            elif is_email:
                username = User.objects.get(email=Id_field).username
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    return render(request, "core/login.html", {
                        "message": "Invalid Credentials",
                        "form":form
                    })
            else:
                return render(request, "core/login.html", {
                        "message": "Invalid Credentials",
                        "form":form
                    })
    else:
        form = Login_form()
        return render(request,"core/login.html",{"form":form})

#logout view
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

#User profile
@login_required
def profile_view(request):
    user = request.user     # Getting the authenticated user 
    context = {
        "username":user.username,
        "Email":user.email,
        "Joined":user.date_joined.date()    
    }
    return render(request,"core/profile.html",context)

@login_required
def dashboard_view(request):
    user = request.user
    context = {
        "username":user.username
    }
    return render(request,"core/dashboard.html",context)