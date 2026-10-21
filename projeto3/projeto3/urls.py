"""
URL configuration for projeto3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # painel administrativo do Django
from django.http import HttpResponse
from django.urls import path, include # path para rotas, include para incluir outras URLs
from rest_framework.routers import DefaultRouter # router que gera rotas para ViewSets
from livros.views import AutorViewSet, LivroViewSet # ViewSets registrados no router


def home(request):
    return HttpResponse("<h1>Livros API</h1><p>Bem-vindo ao projeto de livros.</p>")


router = DefaultRouter()
router.register(r'autores', AutorViewSet)  # registra endpoints para autores: /api/autores/
router.register(r'livros', LivroViewSet)  # registra endpoints para livros: /api/livros/

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),  # rota do Django admin
    path('api/', include(router.urls)),  # inclui rotas geradas pelo router sob o prefixo /api/
]