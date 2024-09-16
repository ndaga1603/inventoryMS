from django.contrib import admin
from .models import Customer, Order, Product, OrderProduct

# Register your models here.
admin.site.register([Customer, Order, Product, OrderProduct]);
