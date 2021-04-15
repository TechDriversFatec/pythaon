from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar_vaga',views.buscarvaga),
    path('cadastrar_curriculo',views.CadastrarCurriculo),
    path('atualizar_curriculo/<str:pk>',views.AtualizarCurriculo),
    path('deletar_curriculo/<str:pk>',views.DeletarCurriculo),
]