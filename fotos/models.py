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
        return self.apellido
    


class Galeria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null= True, blank= False)
    direccion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Obra(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null= True, blank= False)
    ano = models.IntegerField(null= True, blank= False)
    tipo_de_artista = models.ForeignKey(Categoria_artista, on_delete=models.SET_NULL, null= True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.SET_NULL, null= True, blank=True)
    galeria = models.ForeignKey(Galeria, on_delete=models.SET_NULL, null= True, blank=True)
    precio = models.IntegerField(null= True, blank= False)
    vendido = models.CharField(max_length=100,null= True, blank= False)
    
    def __str__(self):
        return self.nombre