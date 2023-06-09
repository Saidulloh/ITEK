from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="POS system API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

api_urlpatterns = [
    path('basket_detail/', include('apps.basket_detail.urls')),
    path('baskets/', include('apps.baskets.urls')),
    path('categories/', include('apps.categories.urls')),
    path('ingredients/', include('apps.ingredients.urls')),
    path('products/', include('apps.products.urls')),
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # api
    path('', include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
