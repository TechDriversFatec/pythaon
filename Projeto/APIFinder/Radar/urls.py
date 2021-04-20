from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('buscar_vaga',views.buscarvaga),
    path('atualizar_vaga/<str:id>',views.updatevaga),
=======
    path('buscar_curriculo/<str:pk>', views.BuscarCurriculo),
>>>>>>> a5e2a788ef2a2af4ae6c41c5cd0e0f1aefab9592
    path('cadastrar_curriculo',views.CadastrarCurriculo),
    path('atualizar_curriculo/<str:pk>',views.AtualizarCurriculo),
    path('deletar_curriculo/<str:pk>',views.DeletarCurriculo),
    path('searchByCargo',views.searchByCargo),
    path('buscaPorVaga/<str:VagaID>/',views.buscarPorVaga),
]

