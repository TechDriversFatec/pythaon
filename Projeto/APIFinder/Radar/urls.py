from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('searchByCargo',views.searchByCargo),
    path('buscaPorVaga/<str:VagaID>/',views.buscarPorVaga),
]
# 