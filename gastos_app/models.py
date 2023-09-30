from django.db import models

from django.db import models

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateTimeField(auto_now_add=True)

class Ingreso(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateTimeField(auto_now_add=True)


