from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    YEAR_CHOICES = {
        ('2015', '2015'),
        ('2016', '2016'),
    }
    year = forms.CharField(choices=YEAR_CHOICES)

    class Meta:
        model = User
        fields = ("username", "email")