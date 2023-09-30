from django.urls import path
from .views import *


urlpatterns = [
    path('gastos/', GastoListCreateView.as_view(), name='gasto-list-create'),
    path('ingresos/', IngresoListCreateView.as_view(), name='ingreso-list-create'),
]