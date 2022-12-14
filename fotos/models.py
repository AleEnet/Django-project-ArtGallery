from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    # apellido
    # edad
    # tecnica
    # foto


class Cuadro(models.Model):
    nombre = models.CharField(max_length=100)
    # # nombre
    # # ano
    # # tecnica
    # # estilo
    # # tamaño
    # # artista
    # # galeria
    # # precio
    # # vendido

class comprador(models.Model):
    nombre = models.CharField(max_length=100)
        # nombre
        # apellido
        # edad
        # domicilio
        # cuadros
