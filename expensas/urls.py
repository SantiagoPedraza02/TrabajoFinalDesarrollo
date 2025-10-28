from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, IngresosViewSet, GastosViewSet


router = DefaultRouter()
router.register(r"categorias", CategoryViewSet)
router.register(r"ingresos", IngresosViewSet)
router.register(r"expensas", GastosViewSet)


urlpatterns = [
path("", include(router.urls)),
]