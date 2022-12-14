from django.urls import path
from . import views

urlpatterns = [
    path("",views.galeria, name = "galeria"),
    path("detalle_artista/<str:pk>",views.detalle_artista, name = "detalle_artista"),
    path("agregar_artista/",views.agregar_artista, name = "agregar_artista"),
]