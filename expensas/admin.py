from django.contrib import admin
from .models import Category, Ingresos, Gastos
# Register your models here.
admin.site.register(Category)
admin.site.register(Ingresos)
admin.site.register(Gastos)