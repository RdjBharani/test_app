from itertools import product
from pyexpat import model
from time import timezone
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class ProductDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, default='')
    cost = models.CharField(max_length=128, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.id

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    class Meta:
        db_table = "product_details"
