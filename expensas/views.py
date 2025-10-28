from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Category, Ingresos, Gastos
from .serializers import CategorySerializer, IngresosSerializer, GastosSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class IngresosViewSet(viewsets.ModelViewSet):
    queryset = Ingresos.objects.all()
    serializer_class = IngresosSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'date']
    ordering_fields = ['date', 'amount']
    ordering = ['-date']


class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'date']
    ordering_fields = ['date', 'amount']
    ordering = ['-date']