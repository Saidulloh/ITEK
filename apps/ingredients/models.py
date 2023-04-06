from django.db import models


class Ingredient(models.Model):
    """
    Model for ingredients
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    image = models.ImageField(
        upload_to='ingredient_images/',
        verbose_name='image'
    )

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'
    
    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'Ingredients'
