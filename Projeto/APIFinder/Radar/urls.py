from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('buscar_vaga/<str:pk>',views.buscarvaga),
    path('inserir_vaga',views.insert_vaga),
    path('atualizar_vaga/<str:pk>',views.updatevaga),
    path('excluir_vaga/<str:pk>',views.delete_vaga),
    path('buscar_curriculo/<str:pk>', views.buscarCurriculo),
    path('inserir_curriculo',views.cadastrarCurriculo),
    path('atualizar_curriculo/<str:pk>',views.atualizarCurriculo),
    path('excluir_curriculo/<str:pk>',views.deletarCurriculo),
    path('busca_VT0/<str:VagaID>',views.buscarPorVagaVT0),
    path('buscaPorVaga/<str:VagaID>',views.buscarPorVaga),
=======
    path('buscar_vaga/<str:pk>',views.View.buscarvaga),
    path('inserir_vaga',views.View.insert_vaga),
    path('atualizar_vaga/<str:pk>',views.View.updatevaga),
    path('excluir_vaga/<str:pk>',views.View.delete_vaga),
    path('buscar_curriculo/<str:pk>', views.View.buscarCurriculo),
    path('inserir_curriculo',views.View.cadastrarCurriculo),
    path('atualizar_curriculo/<str:pk>',views.View.atualizarCurriculo),
    path('excluir_curriculo/<str:pk>',views.View.deletarCurriculo),
    path('buscaPorVaga/<str:VagaID>',views.View.buscarPorVaga),
>>>>>>> fcca48ea868ce599f2ad84196141dd8875571392
]

