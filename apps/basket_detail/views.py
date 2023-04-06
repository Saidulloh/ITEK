from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.basket_detail.models import ProductBasket
from apps.basket_detail.serializers import CreateProductBasketSerializer, ProductBasketSerializer
from apps.baskets.models import Basket


class ProductBasketApiViewSet(ModelViewSet):
    queryset = ProductBasket.objects.all()
    serializer_class = CreateProductBasketSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductBasketSerializer
        return ProductBasketSerializer

    def create(self, request, *args, **kwargs):
        try:
            basket_obj = Basket.objects.get(id=request.data['basket'])
            if basket_obj.qrcode_id == request.data['qrcode_id']:
                basket_products = ProductBasket.objects.filter(basket_id=basket_obj.pk)
                for basket_product in basket_products:
                    if basket_product.product.id == int(request.data['product']):
                        basket_product.amount = int(request.data['amount'])
                        basket_product.save()
                        return Response(
                            data={"ok": f"we finish update product amount to {basket_product.amount}"})
                return super().create(request, *args, **kwargs)
            return Response(data={"Error": "This order is not your!"})
        except Basket.DoesNotExist:
            return Response(data={"Error": "This basket does not exist!"})
