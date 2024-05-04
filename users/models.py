from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=100, blank=False)
    phone_no = models.CharField(max_length=100, blank=False)
    id_no = models.CharField(max_length=100, blank=False)
    is_admin =models.CharField(max_length=20, blank=True)