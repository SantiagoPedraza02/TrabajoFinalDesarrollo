from rest_framework import serializers
from .models import Category, Ingresos, Gastos

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class IngresosSerializer(serializers.ModelSerializer):
    CategoryName = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Ingresos
        fields = ['id', 'amount', 'date', 'description', 'category', 'CategoryName']

class GastosSerializer(serializers.ModelSerializer):
    CategoryName = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Gastos
        fields = ['id', 'amount', 'date', 'description', 'category', 'CategoryName']
