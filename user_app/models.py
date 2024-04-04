from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    interests = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    CATEGORY = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('children', 'Children'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY)

    def __str__(self):
        return self.name