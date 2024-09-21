from django.contrib import admin
<<<<<<< HEAD
from .models import Customer, Order, Product, OrderProduct

# Register your models here.
admin.site.register([Customer, Order, Product, OrderProduct]);
=======
from .models import *



admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
>>>>>>> 078c2d88e99555ac382a79e5984c9447c64fa914
