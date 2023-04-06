from django.db import models

from apps.ingredients.models import Ingredient
from apps.categories.models import Category


class Product(models.Model):
    """
    Model for products
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        verbose_name='ingredient'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        verbose_name='category',
        null=True, 
        blank=True
    )
    description = models.TextField(
        verbose_name='description'
    )
    image = models.ImageField(
        upload_to='product_images/',
        verbose_name='image'
    )

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'
