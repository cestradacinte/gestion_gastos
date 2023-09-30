from rest_framework import generics
from .models import Gasto, Ingreso
from .serializers import GastoSerializer, IngresoSerializer

class GastoListCreateView(generics.ListCreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class IngresoListCreateView(generics.ListCreateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer