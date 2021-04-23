from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('buscar_vaga',views.buscarvaga),
    path('insert_vaga',views.insert_vaga),
    path('update_vaga',views.update_vaga),
    path('delete_vaga/<str:pk>',views.delete_vaga),
    path('cadastrar_curriculo',views.CadastrarCurriculo),
    path('atualizar_curriculo/<str:pk>',views.AtualizarCurriculo),
    path('deletar_curriculo/<str:pk>',views.DeletarCurriculo),
    path('searchByCargo',views.searchByCargo),
    path('buscaPorVaga/<str:VagaID>/',views.buscarPorVaga),
]

