from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
# from .forms import LoginForm

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "login/",
        LoginView.as_view(template_name="authentication/login.html", next_page="home"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
]
