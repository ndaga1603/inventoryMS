from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    USER_TYPES = (
        (1, 'Manager'),
        (2, 'Procurement Officer'),
        (3, 'Sales Officer'),
    )

    GENDER = (
        (1, "Male"),
        (2, "Female")
    )

    username = None
    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'  # set the email field as the username field for authentication
    REQUIRED_FIELDS = [] # remove username from required fields 
    
    objects = CustomUserManager()
    
    class Meta:
        db_table = 'user'
        ordering = ["id"]
        

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to='customer_pics', default='default.jpg')
    
    class Meta:
        db_table = 'customer'
        
    def __str__(self):
        return self.full_name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_pics', default='default.jpg')
    
    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
    
class Order(models.Model):
    ORDER_STATUS = (
        (1, 'Pending'),
        (2, 'Completed'),
        (3, 'Cancelled'),
    )
    
    PAYMENT_STATUS = (
        (1, 'Pending'),
        (2, 'Paid'),
    )
    
    order_id = models.CharField(max_length=100, unique=True)
    order_status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    payment_status = models.PositiveSmallIntegerField(choices=PAYMENT_STATUS)
    placed_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'order'
    
    def __str__(self):
        return self.order_id
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'order_product'
    
    def __str__(self):
        return self.product.name
    