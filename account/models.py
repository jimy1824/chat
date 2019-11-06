from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=25, choices=GENDER, default=MALE)
    profile_picture = models.ImageField(upload_to='profile-pictures/', blank=True)
    email = models.EmailField(unique=True, max_length=75)
    username = models.CharField(null=True, max_length=150, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return 'Id:{0} Name :{1} {2}, email: {3}'.format(self.id, self.first_name, self.last_name, self.email)
