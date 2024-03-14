from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.choices import USER_TYPE
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255, unique=True)
    phone_number = models.IntegerField()
    password = models.CharField(max_length = 255)
    user_type = models.CharField(choices = USER_TYPE, max_length = 255)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    