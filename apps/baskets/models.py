from django.db import models


class Basket(models.Model):
    """
    Model for baskets
    """
    qrcode_id = models.CharField(
        max_length=256,
        verbose_name='qrcode_id'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    
    def __str__(self):
        return f'{self.id} -- {self.qrcode_id}'
    
    class Meta:
        verbose_name = 'basket'
        verbose_name_plural = 'Baskets'
