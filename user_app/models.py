from django.db import models
from django.contrib.auth.models import User
from random import randint
class CustomUser(User):
    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    interests = (
        ('sports', 'Sports'),
        ('music', 'Music'),
        ('books', 'Books'),
        ('movies', 'Movies'),
        ('travel', 'Travel'),
        ('food', 'Food'),
    )
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=gender, blank=True)
    interests = models.CharField(max_length=20, choices=interests, blank=True)

class Product(models.Model):
    user_category = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('children', 'Children'),
    )
    product_category = (
        ('sports', 'Sports'),
        ('music', 'Music'),
        ('books', 'Books'),
        ('movies', 'Movies'),
        ('travel', 'Travel'),
        ('food', 'Food'),
    )
    name = models.CharField(max_length=100)
    user_category = models.CharField(max_length=10, choices=user_category)
    product_category = models.CharField(max_length=10, choices=product_category)
    random_rating = randint(0, 100)
    rating = models.IntegerField(default=random_rating)
    from_age = models.DateField(null=True, blank=False)
    under_age = models.DateField(null=True, blank=False)