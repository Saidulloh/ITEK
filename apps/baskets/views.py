from rest_framework.viewsets import ModelViewSet

from apps.baskets.models import Basket
from apps.baskets.serializers import BasketSerializer


class BasketApiViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
