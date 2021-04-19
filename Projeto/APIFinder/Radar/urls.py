from django.urls import path
from . import views

urlpatterns = [
    path('buscar_curriculo/<str:pk>', views.BuscarCurriculo),
    path('cadastrar_curriculo',views.CadastrarCurriculo),

]

