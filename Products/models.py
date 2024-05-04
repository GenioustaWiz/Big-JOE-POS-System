from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    cost_price = models.CharField(max_length=100)
    selling_price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)