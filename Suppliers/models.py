from django.db import models

# Create your  models here.
class supplier(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content_supplied = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)