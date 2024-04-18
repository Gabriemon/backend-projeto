from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from jogos.models import Jogos
from jogos.serializer import JogosSerializer


class jogosViewSet(viewsets.ModelViewSet):
    """Endpoint para exibir dados de alunos"""
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer 
