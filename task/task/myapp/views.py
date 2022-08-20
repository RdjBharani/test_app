from django.shortcuts import render
from rest_framework import permissions, response, status, views
from myapp import controllers, serializers
import ast


class Orders(views.APIView):

    def post(self, request):
            data = request.data
            user = request.user
            product_list = data.get("product_list", "")
            product_data = []
            if product_list:
                try:
                    teststr = f"{product_list}"
                    product_data = ast.literal_eval(teststr)
                except Exception:
                    return response.Response(
                        {"result": False, "msg": "Invalid product_ids."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if not type(product_data) == list:
                    return response.Response(
                        {
                            "result": False,
                            "msg": "product_ids should be list.",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            store_item_mapping_controller = controllers.StoreItemMappingController()
            store_item_mapping_ids = []
            quantity_list = []
            for data in product_data:
                store_item_mapping_ids.append(data['store_item_mapping_id'])
                quantity_list.append(data["quantity"])
            items = store_item_mapping_controller.get_by_id(store_item_mapping_ids = store_item_mapping_ids)
            order_controller = controllers.OrdersController()
            order_details = order_controller.create(
                user=user,
                items=items,
                quantity_list=quantity_list
            )
            serialized_data = serializers.OrderSerializers(instance=order_details, many=True).data
            return response.Response(
            {"result": True, "msg": "success", "data": serialized_data},
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        data = request.query_params
        user = request.user
        order_ids_str = data.get("order_ids", "")
        order_id = data.get("order_id", "")
        store_id = data.get("store_id", "")

        order_controller = controllers.OrdersController()

        if order_id:
            if str(order_id).isdigit() is False:
                return response.Response(
                    {
                        "result": False,
                        "msg": "order_id should be integer",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            
            order_details = order_controller.get_by_id(order_id=order_id)

            serialized_data = serializers.OrderSerializers(instance=order_details, many=False).data
            return response.Response(
                {"result": True, "msg": "success", "data": serialized_data},
                status=status.HTTP_200_OK,
            )
        order_ids = []
        if order_ids_str:
            try:
                teststr = f"{order_ids_str}"
                order_ids = ast.literal_eval(teststr)
            except Exception:
                return response.Response(
                    {"result": False, "msg": "Invalid order_ids."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if not type(order_ids) == list:
                return response.Response(
                    {
                        "result": False,
                        "msg": "order_ids should be list.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            order_details = order_controller.get_by_ids(order_ids=order_ids)

            serialized_data = serializers.OrderSerializers(instance=order_details, many=True).data
            return response.Response(
                {"result": True, "msg": "success", "data": serialized_data},
                status=status.HTTP_200_OK,
            )
        
        if store_id:
            if str(store_id).isdigit() is False:
                return response.Response(
                    {
                        "result": False,
                        "msg": "store_id should be integer",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            
            order_details = order_controller.get_by_store_id(store_id=store_id)

            serialized_data = serializers.OrderSerializers(instance=order_details, many=True).data
            return response.Response(
                {"result": True, "msg": "success", "data": serialized_data},
                status=status.HTTP_200_OK,
            )

        if not order_ids or not order_id or not store_id:
            order_details = order_controller.get_by_user(user=user)

            serialized_data = serializers.OrderSerializers(instance=order_details, many=True).data
            return response.Response(
                {"result": True, "msg": "success", "data": serialized_data},
                status=status.HTTP_200_OK,
            )
    
    def put(self, request):
            data = request.data
            user = request.user
            order_id = data.get("order_id", "")
            status_id = data.get("status_id", "")
            
            if status_id:
                if str(status_id).isdigit() is False:
                    return response.Response(
                        {
                            "result": False,
                            "msg": "status_id should be integer",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if order_id:
                if str(order_id).isdigit() is False:
                    return response.Response(
                        {
                            "result": False,
                            "msg": "order_id should be integer",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            order_controller = controllers.OrdersController()
            order_details = order_controller.get_by_id(order_id=order_id)
            order_details = order_controller.update_status(order_details=order_details, status_id=status_id)
            serialized_data = serializers.OrderSerializers(instance=order_details, many=False).data
            return response.Response(
            {"result": True, "msg": "success", "data": serialized_data},
            status=status.HTTP_200_OK
        )

