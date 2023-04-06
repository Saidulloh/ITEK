from django.contrib import admin

from apps.basket_detail.models import ProductBasket


@admin.register(ProductBasket)
class ProductBasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'qrcode_id', )
