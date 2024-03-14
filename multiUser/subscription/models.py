from django.db import models
from authentication.models import User
# Create your models here.

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits = 10, decimal_places = 4)
    description = models.TextField(max_length = 255)
    
    def __str__(self):
        return f"Subscribe to a {self.name} plan to {self.description} and pay just {self.price}$"
    
    
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete = models.CASCADE)
    status = models.BooleanField(default = False)
    expiration_date = models.DateField()