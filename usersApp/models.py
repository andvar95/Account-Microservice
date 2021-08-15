from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class User(AbstractUser):
    phone = models.TextField(max_length=10,blank=True)
    address = models.TextField(max_length=50,blank=True)
    email = models.EmailField(('email address'),   unique=True,error_messages={
            'unique': ("A user with that email already exists."),
        },)
    username = models.CharField(('username'),max_length=150,unique=True)