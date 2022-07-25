from statistics import mode
from django.contrib import admin

from myapp import models

admin.site.register(models.Category)
admin.site.register(models.ProductDetails)
