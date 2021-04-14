from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar_vaga',views.buscarvaga),
    path('insert_vaga',views.insert_vaga),
    path('delete_vaga',views.delete_vaga),
]