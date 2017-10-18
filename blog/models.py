from django.db import models

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=16, unique=True)
    email = models.CharField(default='abc@example.com', unique=True, max_length=75)
    password_hash = models.CharField(max_length=256)

    def __str__(self):
        return self.username
