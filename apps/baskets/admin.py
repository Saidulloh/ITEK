from django.contrib import admin

from apps.baskets.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'qrcode_id', 'created_at', )
