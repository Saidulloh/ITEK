from rest_framework import serializers

from apps.baskets.models import Basket
from apps.basket_detail.models import ProductBasket
from apps.basket_detail.serializers import ProductBasketSerializer


class BasketSerializer(serializers.ModelSerializer):
    basket_products = ProductBasketSerializer(read_only=True, many=True)
    sum_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Basket
        fields = (
            'id',
            'qrcode_id',
            'created_at',
            'sum_price',
            'basket_products'
        )

    def get_sum_price(self, obj):
        basket = ProductBasket.objects.filter(basket_id=obj.id)
        return sum([int(i.product.price) * int(i.amount) for i in basket])