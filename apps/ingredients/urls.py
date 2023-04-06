from rest_framework.routers import DefaultRouter

from apps.ingredients.views import IngredientApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=IngredientApiViewSet
)

urlpatterns = router.urls
