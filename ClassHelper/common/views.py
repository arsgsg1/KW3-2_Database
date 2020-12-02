from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return redirect(request, 'common/login.html')


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/campus')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def update(request):
    return render(request, 'common/user_update.html')


def lookup(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        userinfo = CustomUser.objects.filter(username=cur_user.username).values()
        print(userinfo)
        context = {
            'userinfo' : userinfo
        }
        return render(request, 'common/lookup.html', context)
    return redirect('common/login.html')