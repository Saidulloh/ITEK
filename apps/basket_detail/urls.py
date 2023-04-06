from rest_framework.routers import DefaultRouter

from apps.basket_detail.views import ProductBasketApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=ProductBasketApiViewSet
)

urlpatterns = router.urls
