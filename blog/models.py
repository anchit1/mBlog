from django.db import models

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=16, unique=True)
    email = models.CharField(default='abc@example.com', unique=True, max_length=75)
    password_hash = models.CharField(max_length=256)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):

    publish_date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
