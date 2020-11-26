from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_password = models.CharField(max_length=20)
    signup_date = models.DateTimeField('date published')

    def __str__(self):
        return self.user_id
