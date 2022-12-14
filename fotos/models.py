from django.db import models

class Categoria_proyecto(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre



class Categoria_artista(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    categoria_proyecto = models.ForeignKey(Categoria_proyecto, on_delete=models.SET_NULL, null= True, blank=True)
    imagen = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.nombre


class Artista(models.Model):
    categoria = models.ForeignKey(Categoria_artista, on_delete=models.SET_NULL, null= True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(null= False, blank= False)

    def __str__(self):
        return self.descripcion
    

class Obra(models.Model):
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


class Galeria(models.Model):
    nombre = models.CharField(max_length=100)
    # nombre
    # apellido
    # edad
    # domicilio
    # cuadros
