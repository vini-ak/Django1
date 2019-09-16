from django.contrib import admin
from django.urls import path
from .views import *

# Executa o método listar_tarefas da view
urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
]
