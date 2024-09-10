from django.db import models
from django.contrib.auth.models import AbstractUser

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
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES)
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'  # set the email field as the username field for authentication
    REQUIRED_FIELDS = [] # remove username from required fields 
