from rest_framework import serializers

from apps.basket_detail.models import ProductBasket
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductBasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductBasket
        fields = (
            'id',
            'qrcode_id',
            'amount',
            'basket',
            'product'
        )

    def get_product(self, obj):
        data = Product.objects.get(id=obj.product.id)
        return ProductSerializer(data).data


class CreateProductBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBasket
        fields = '__all__'
