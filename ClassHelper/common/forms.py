from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    division = forms.CharField(max_length=25)
    phone_number = forms.CharField(max_length=25)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "division", "phone_number")