from django.urls import path
from . import views

urlpatterns = [
    path("",views.galeria, name = "galeria"),
    path("agregar_artista/",views.agregar_artista, name = "agregar_artista"),
    path("agregar_obra/",views.agregar_obra, name = "agregar_obra"),
    path("agregar_galeria/",views.agregar_galeria, name = "agregar_galeria"),
    path("buscar/",views.buscar,name = "buscar"),
    
]