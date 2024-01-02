from django.urls import path

from .views import *


urlpatterns = [
    path("user/register",name="sign-up"),
    path("user/login",name="login"),
    path("user/profile",name="profile")
]