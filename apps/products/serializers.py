from rest_framework import serializers

from apps.products.models import Product
from apps.ingredients.models import Ingredient
from apps.ingredients.serializers import IngredientSerializer
from apps.categories.serializers import CategorySerializer


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'description',
            'image',
            'ingredients'
        )

    def get_ingredients(self, obj):
        product = Product.objects.get(id=obj.id)
        instance = Ingredient.objects.filter(id__in=[i.id for i in product.ingredient.all()])
        serializer = IngredientSerializer(instance, many=True)
        return serializer.data
