from rest_framework.routers import DefaultRouter # router automático do DRF
from .views import PessoasViewSet # ViewSet que fornece endpoints para Pessoas
router = DefaultRouter()
router.register(r'pessoas', PessoasViewSet) # registra rotas: /pessoas/ (list/create) e /pessoas/{pk}/
urlpatterns = router.urls # expõe as rotas geradas pelo router