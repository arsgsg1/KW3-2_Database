from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        return render(request, "campus/index.html")
    else:
        return redirect('/common/login')