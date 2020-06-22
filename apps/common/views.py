from django.shortcuts import render

from django.views.generic import TemplateView,CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # to inforce user to login before open dashboard page

class HomeView(TemplateView):
    template_name="common/home.html"

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "common/register.html"
    success_url = reverse_lazy('home') # tell djnago where to go when signup process finish successfuly

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "common/dashboard.html"
    login_url = "login"