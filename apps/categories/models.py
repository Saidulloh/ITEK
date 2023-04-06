from django.db import models


class Category(models.Model):
    """
    Model for categories
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
