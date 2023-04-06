from rest_framework.viewsets import ModelViewSet

from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductCreateSerializer


class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'retrieve', 'update']:
            return ProductCreateSerializer
        return ProductSerializer
