"""Floricultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cliente.views import home
from cliente.views import lista
from cliente.views import cadastrar_cliente
from cliente.views import atualizar_cliente
from cliente.views import deletar_cliente


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('lista/', lista, name='lista'),
    path('cadastrar_cliente/', cadastrar_cliente, name='Cadastro Cliente'),
    path('atualizar_cliente/<int:pk>',atualizar_cliente, name='Atualizar Cliente'),
    path('deletar_cliente/<int:pk>',deletar_cliente, name='Deletar Cliente'),
]
#PARA QUE POSSA ALTERAR ALGUM OBJETO, É NECESSÁRIO QUE PASSE UMA REFERÊNCIA PARA O MESMO
#ENTÃO, CRIAMOS UMA 'PRIMARY_KEY' PARA QUE O OBJETO POSSA SER ENCONTRADO MAIS FACILMENTE