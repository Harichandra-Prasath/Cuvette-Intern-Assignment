from django.urls import path

from .views import *


urlpatterns = [
    path("accounts/register/",register_view,name="register"),
    path("accounts/login/",login_view,name="login"),
    path("accounts/logout/",logout_view,name="logout"),
    path("users/profile/",profile_view,name="profile"),
    path("users/dashboard/",dashboard_view,name="dashboard"),

]