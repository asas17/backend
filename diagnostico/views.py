from rest_framework import viewsets
from .serializer import DiagnosticoSerializer
from .models import Diagnostico

# Create your views here.
class DiagnosticoView(viewsets.ModelViewSet):
    serializer_class = DiagnosticoSerializer
    queryset = Diagnostico.objects.all()
