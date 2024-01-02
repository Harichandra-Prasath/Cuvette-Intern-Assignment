from django.urls import path

from .views import *


urlpatterns = [
    path("user/register/",register_view,name="register"),
    path("user/login/",login_view,name="login"),
    #path("user/profile",name="profile")
    path("user/logout/",logout_view,name="logout")
]