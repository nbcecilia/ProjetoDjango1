from django.urls import path, include # roteamento
from rest_framework.routers import DefaultRouter # router para ViewSets
from .views import salvar_comentario, ComentarioViewSet # views do app
router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet) # registra o ViewSet em /api/
urlpatterns = [
 path('', salvar_comentario, name='salvar_comentario'), # formulário/lista (GET) e salva (POST)
 path('', include(router.urls)), # inclui rotas da API geradas pelo router (ex.: /comentarios/,/comentarios/<pk>/)
]