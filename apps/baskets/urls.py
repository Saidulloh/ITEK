from rest_framework.routers import DefaultRouter

from apps.baskets.views import BasketApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=BasketApiViewSet
)

urlpatterns = router.urls
