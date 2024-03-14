from django.db import models
from authentication.models import User
# Create your models here.

class Image(models.Model):
    owner = models.ForeignKey(User, related_name='Images', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.name
