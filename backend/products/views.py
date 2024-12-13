from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Products, StockManagement, Variants
from .serializers import ProductSerializer
from decimal import Decimal
#from .pagination import ProductPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    #pagination_class = ProductPagination  # Set the pagination class

    @action(detail=True, methods=["post"],url_path="add-stock")
    def add_stock(self, request, pk=None):
        try:
            product = self.get_object()
            variant_id = request.data.get("variant_id")
            print(variant_id)
            quantity = request.data.get("quantity")
            options = request.data.get("options")

            if not variant_id or not quantity:
                return Response(
                    {"error": "variant_id and stock_change are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            variant = Variants.objects.get(id=variant_id, product=product)
            variant.quantity += Decimal(quantity)
            variant.options.extend(options)
            variant.save()
           # sub_variant.stock += Decimal(stock_change)
            #sub_variant.save()
            return Response({"message": "Stock added successfully."}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=["post"],url_path="remove-stock")
    def remove_stock(self, request, pk=None):
        try:
            product = self.get_object()
            variant_id = request.data.get("variant_id")
            quantity = request.data.get("quantity")
            options = request.data.get("options")

            if not variant_id or not quantity:
                return Response(
                    {"error": "sub_variant_id and stock_change are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            variant = Variants.objects.get(id=variant_id, product=product)
            if variant.quantity < int(quantity):
                return Response(
                    {"error": "Not enough stock available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if quantity:
                variant.quantity -= int(quantity)
            if options:
                update_list = []
                for opt_data in variant.options:
                    if opt_data not in options:
                        update_list.append(opt_data)
                variant.options = update_list


            variant.save()

            # StockManagement.objects.create(
            #     variant=variant,
            #     change=-Decimal(stock_change),
            #     reason="SALE",
            # )
            return Response({"message": "Stock removed successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)