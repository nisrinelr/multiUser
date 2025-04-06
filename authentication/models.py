from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.choices import USER_TYPE
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email, password, and required fields.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Using EmailField for email addresses
    phone_number = models.CharField(max_length=15)  # Changed to CharField for flexibility
    user_type = models.CharField(choices=[('BETA USER', 'Beta user'), ('COMPANY USER', 'Company user'), ('PLAN SUBSCRIBER', 'Plan subscriber')], max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = UserManager()  # Set the custom manager here

    def __str__(self):
        return self.email  # Use email for string representation of the user

    
    
    