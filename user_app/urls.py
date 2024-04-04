from django.urls import path
from .views import *

urlpatterns = [
    path('product/', products_for_user),
    path('add-user/', create_user),
    path('add-product/', create_product),
]
