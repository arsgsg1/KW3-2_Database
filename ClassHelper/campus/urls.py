from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'campus'

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.subject_apply, name='subject_apply'),
]