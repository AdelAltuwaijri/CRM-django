from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False,help_text="Optional")
    last_name = forms.CharField(max_length=20, required=False,help_text="Optional")
    email = forms.CharField(max_length=200,help_text="Enter a valid enail address")
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]