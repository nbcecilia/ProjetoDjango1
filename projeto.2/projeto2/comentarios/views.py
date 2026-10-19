from django.shortcuts import render, redirect # renderiza templates, redirect redireciona
from .models import Comentario # modelo Comentario
from rest_framework import viewsets # viewsets do DRF
from .serializers import ComentarioSerializer # serializer do Comentario
def salvar_comentario(request):
 # salva comentário enviado via POST, caso contrário mostra o formulário
 if request.method == 'POST':
  autor = request.POST.get('autor')
  texto = request.POST.get('texto')
  comentario = Comentario(autor=autor, texto=texto)
  comentario.save()
 return redirect('salvar_comentario')
 comentarios = Comentario.objects.all().order_by('-data_criacao') # lista comentários (mais novos primeiro)
 return render(request, 'comentarios/formulario.html', {'comentarios': comentarios})
class ComentarioViewSet(viewsets.ModelViewSet):
 queryset = Comentario.objects.all().order_by('-data_criacao') # queryset base
 serializer_class = ComentarioSerializer # serializer usado