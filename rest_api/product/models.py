from itertools import product
from django.db import models


# Create your models here.

class Discount(models.Model):
    product_discount = models.FloatField()
    discount_amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    flat_amount = models.FloatField()
    percentage_amount = models.FloatField()

    class Meta:
        def __str__(self):
            return self.discount_amount


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    '''discount = models.ForeignKey(Discount, on_delete=models.CASCADE)'''
    

    class Meta:
        def __str__(self):
            return self.title

