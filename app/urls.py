from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .api.product import ProductViewSet
from .api.category import CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
