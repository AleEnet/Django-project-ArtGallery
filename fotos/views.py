from django.shortcuts import render
from .models import  Categoria_proyecto, Categoria_artista, Artista


def galeria(request):
    categorias_proyectos = Categoria_proyecto.objects.all()
    categorias_artistas = Categoria_artista.objects.all()
    context = {"categorias_proyectos" : categorias_proyectos, "categorias_artistas" : categorias_artistas}
    return render(request, "galeria.html", context )


def agregar_artista(request):
    categorias_artistas = Categoria_artista.objects.all()
    context = {"categoria_artista":categorias_artistas}
    
    if request.method == "POST":
        data=request.POST
        imagen = request.FILES.get("imagen")
        print("data:",data)
        print("imagen:",imagen)

    return render(request, "agregar_artista.html",context)


def detalle_artista(request, pk):
    artista  = Artista.objects.get(id=pk)
           
    return render(request, "detalle_artista.html", {"artista": artista})
