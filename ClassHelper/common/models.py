from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    term = models.CharField(max_length=25, null=True)
    division = models.CharField(max_length=25, null=True)
    phone_number = models.CharField(max_length=25, null=True)