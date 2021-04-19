from django.urls import path
from . import views

urlpatterns = [
    path('buscar_curriculo/<str:pk>', views.BuscarCurriculo),
    path('cadastrar_curriculo',views.CadastrarCurriculo),
    path('atualizar_curriculo/<str:pk>',views.AtualizarCurriculo),
    path('deletar_curriculo/<str:pk>',views.DeletarCurriculo),
    path('searchByCargo',views.searchByCargo),
    path('buscaPorVaga/<str:VagaID>/',views.buscarPorVaga),
    path('insert_vaga',views.insert_vaga),
    path('delete_vaga/<str:pk>',views.delete_vaga),
]

