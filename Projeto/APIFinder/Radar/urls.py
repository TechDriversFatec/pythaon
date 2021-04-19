from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('buscar_curriculo/<str:pk>', views.BuscarCurriculo),
    path('cadastrar_curriculo',views.CadastrarCurriculo),
]
=======
    path('', views.home, name='home'),
    path('searchByCargo',views.searchByCargo),
    path('buscaPorVaga/<str:VagaID>/',views.buscarPorVaga),
]
# 
>>>>>>> 91d0321a0067f8d5f5124fb1f0fe0aa33bbd39cf
