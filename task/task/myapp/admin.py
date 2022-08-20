from django.contrib import admin
from myapp import models

admin.site.register(models.StoreDetails)
admin.site.register(models.ItemDetails)
admin.site.register(models.OrderDetails)
admin.site.register(models.StoreItemDetailsMapping)