from django.contrib import admin
from django.urls import path,include
from products.views import get_products

urlpatterns = [
    path('<slug>/',get_products,name='index'),
   
]
