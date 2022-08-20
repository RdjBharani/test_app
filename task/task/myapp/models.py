from django.conf import settings
from django.contrib import auth
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


User = auth.get_user_model()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class StoreDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, blank=True, default="")
    phone_number = models.CharField(max_length=32, blank=True, default="")
    address = models.CharField(max_length=32, blank=True, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "store_details"

class ItemDetails(models.Model):
    name = models.CharField(max_length=128, blank=True, default='')
    price = models.CharField(max_length=128, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.name

    class Meta:
        db_table = "item_details"

class StoreItemDetailsMapping(models.Model):
    store = models.ForeignKey(
        StoreDetails, on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        ItemDetails, on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_createdby"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_updatedby"
    )

    def __unicode__(self):
        return self.id

    def __str__(self):
        return f"{self.store.name}-{self.item.name}"

    class Meta:
        db_table = "store_item_mapping"


class OrderDetails(models.Model):
    STATUS_TYPES = ((1, "PACKED"), (2, "TRANSIT"), (3, "DELIVERED"))
    product = models.ForeignKey(StoreItemDetailsMapping, on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=STATUS_TYPES)
    quantity = models.CharField(max_length=64, blank=True,default='')
    total_amount = models.CharField(max_length=64, blank=True,default='')
    created_on = models.CharField(max_length=64, blank=True,default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return f"{self.product.item.name}-{self.product.store.name}"

    class Meta:
        db_table = "order_details"

