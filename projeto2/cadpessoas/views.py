
from rest_framework import viewsets # viewsets para criar CRUD da API automaticamente
from .models import Pessoas # modelo Pessoas do app
from .serializers import PessoasSerializer # serializer para o modelo Pessoas
from rest_framework import viewsets  # viewsets para criar CRUD da API automaticamente
# - fornece endpoints padrão (list, retrieve, create, update, destroy) pelo ModelViewSet,
class PessoasViewSet(viewsets.ModelViewSet):
 queryset = Pessoas.objects.all().order_by('id') # queryset base, ordenado por id
 serializer_class = PessoasSerializer # serializer usado para (de)serializar Pessoas