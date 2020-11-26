from django import forms
from .models import *
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id']
        label = {
            'user_id' : '아이디',
            'user_password' : '비밀번호',
        }