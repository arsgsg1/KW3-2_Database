from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(
        request,
        'example/index.html',
        {}
    )

def signup(request):
    if request.method == 'POST':
        print('n')
    else:
        return render(
            request,
            'example/signup.html',
            {}
        )