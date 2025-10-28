from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    TYPE_CHOICES = (
        ('ingresos', 'Ingresos'),
        ('gastos', 'Gastos'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.type})"
    

class Ingresos(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, limit_choices_to={'type': 'ingresos'})

    def __str__(self):
        return f"{self.amount} | +{self.date} | {self.category.name}"
        
class Gastos(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, limit_choices_to={'type': 'gastos'})

    def __str__(self):
        return f"{self.amount} | -{self.date} | {self.category.name}"