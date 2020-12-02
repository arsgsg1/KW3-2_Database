from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'campus'

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.subject_apply, name='subject_apply'),
    path('subject_eval/<str:subject_id>', views.subject_eval, name='subject_eval'),
    path('grade/', views.grade, name='grade'),
]