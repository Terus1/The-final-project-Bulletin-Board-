from allauth.account.views import login
from allauth.conftest import user
from allauth.mfa.views import authenticate

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from .forms import CustomSignupForm


class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/accounts/login'
    template_name = 'account/signup.html'
