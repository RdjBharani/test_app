from itertools import product
from myapp import models
from django.contrib import auth
from django.core import exceptions, validators
import datetime

User = auth.get_user_model()

class OrdersController:

    def create(
        self,
        user: User,
        items: list,
        quantity_list: list,
        status=2
    ) -> models.OrderDetails:
        now = datetime.datetime.now()
        objs = [models.OrderDetails(
                    product=product,
                    quantity=quantity,
                    total_amount=str(int(quantity) * int(product.item.price)),
                    created_by=user,
                    status=status,
                    created_on=now
            )
                for product, quantity in zip(items, quantity_list)
            ]
        models.OrderDetails.objects.bulk_create(
            objs=objs
        )
        return models.OrderDetails.objects.filter(created_on=now)

    def get_by_id(self, order_id: int) -> models.OrderDetails:
        return models.OrderDetails.objects.get(id=order_id)
    
    def get_by_ids(self, order_ids: list) -> models.OrderDetails:
        return models.OrderDetails.objects.filter(id__in=order_ids)
    
    def get_by_user(self, user: User) -> models.OrderDetails:
        return models.OrderDetails.objects.filter(created_by=user)
    
    def get_by_store_id(self, store_id: int) -> models.OrderDetails:
        return models.OrderDetails.objects.filter(product__store_id=store_id)
    
    def update_status(self, order_details: models.OrderDetails, status_id: int):
        order_details.status = status_id
        order_details.save()
        return order_details

class StoreItemMappingController:

    def get_by_id(self, store_item_mapping_ids: list) -> models.StoreItemDetailsMapping:
        return models.StoreItemDetailsMapping.objects.filter(id__in= store_item_mapping_ids)
