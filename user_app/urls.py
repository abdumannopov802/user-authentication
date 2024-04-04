from django.urls import path
from .views import *

urlpatterns = [
    path('product/', products_for_user),
]
