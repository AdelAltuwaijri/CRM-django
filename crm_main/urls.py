"""crm_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import reverse_lazy
from apps.common.views import HomeView,SignUp, DashboardView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name="home"),
    path('registration/',SignUp.as_view(),name='registration'),
    path("login/",auth_views.LoginView.as_view(template_name="common/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page='home'),name="logout"),
    path("dashboard/",DashboardView.as_view(),name="dashboard"),
    path("changepassword/",
            auth_views.PasswordChangeView.as_view(
                template_name="common/changepassword.html",success_url=reverse_lazy('home')),
                name="changepassword"),
]