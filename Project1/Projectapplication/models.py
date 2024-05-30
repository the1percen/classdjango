from django.db import models

# Create your models here.
class registration(models.Model):
    email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)