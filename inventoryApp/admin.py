from django.contrib import admin
from .models import User,Customer,Product,Order,OrderProduct

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)

# Register your models here.
