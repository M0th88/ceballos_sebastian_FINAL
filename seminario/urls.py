from django.urls import path
from .views import index
from .controllers.inscrito_views import (
    InscritoListView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView
)
from .controllers.institucion_views import institucion_list, institucion_detail
from .controllers.api_views import autor_info, InscritoAPI, InstitucionAPI  # Importar la nueva API

urlpatterns = [
    path('', index, name='index'),  # Ruta principal (raíz)
    path('inscritos/', InscritoListView.as_view(), name='inscrito_list'),
    path('inscritos/add/', InscritoCreateView.as_view(), name='inscrito_add'),
    path('inscritos/edit/<int:pk>/', InscritoUpdateView.as_view(), name='inscrito_edit'),  # Editar
    path('inscritos/delete/<int:pk>/', InscritoDeleteView.as_view(), name='inscrito_delete'),  # Eliminar
    path('instituciones/', institucion_list, name='institucion_list'),
    path('instituciones/<int:id>/', institucion_detail, name='institucion_detail'),
    path('api/autor/', autor_info, name='autor_info'),
    path('api/inscritos/', InscritoAPI.as_view(), name='inscrito_api'),
    path('api/instituciones/', InstitucionAPI.as_view(), name='institucion_api'),  # Nueva ruta
    
]
