from rest_framework import serializers

from myapp import models

class StoreItemMappingSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='item.name')
    item_price = serializers.ReadOnlyField(source='item.price')
    store_name = serializers.ReadOnlyField(source='store.name')
    store_address = serializers.ReadOnlyField(source='store.address')
    class Meta:
        model = models.StoreItemDetailsMapping
        fields = ["id","store_name","store_address","item_name","item_price"]


class OrderSerializers(serializers.ModelSerializer):
    order_id = serializers.ReadOnlyField(source="id")
    product = StoreItemMappingSerializer()
    order_status = serializers.SerializerMethodField()

    def get_order_status(self, obj):
        return str(obj.get_status_display().lower())

    class Meta:
        model = models.OrderDetails
        fields = ["order_id","product", "quantity", "total_amount","order_status"]