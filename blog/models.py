from django.db import models

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password_hash = models.CharField(max_length=64)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name;