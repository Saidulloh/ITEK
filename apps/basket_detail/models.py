from django.db import models

from apps.products.models import Product
from apps.baskets.models import Basket


class ProductBasket(models.Model):
    """
    Model for appending products to basket
    """
    qrcode_id = models.CharField(
        max_length=256,
        verbose_name='qrcode_id'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        related_name='product_basket',
        verbose_name='product_basket'
    )
    amount = models.SmallIntegerField(
        verbose_name='amount'
    )
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        related_name='basket_products',
        verbose_name='basket_products'
    )

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'product in basket'
        verbose_name = 'Products in baskets'
