from rest_framework.viewsets import ModelViewSet

from apps.ingredients.models import Ingredient
from apps.ingredients.serializers import IngredientSerializer


class IngredientApiViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
