from django.shortcuts import render, redirect
from .models import  *


def galeria(request):
    categoria = request.GET.get("categoria")
    categorias_proyectos= Categoria_proyecto.objects.all()
    
    if categoria == None or categoria == "Artistas":
        elementos = Categoria_artista.objects.all()
        
    elif categoria == "Obras":
        elementos = Obra.objects.all()
    
    else:
        elementos = Galeria.objects.all()


    context = {"categorias_proyectos" : categorias_proyectos, "elementos" : elementos}
    return render(request, "galeria.html", context )


def agregar_artista(request):
    categorias_artistas = Categoria_artista.objects.all()
    context = {"categoria_artista":categorias_artistas}
    
    if request.method == "POST":
        data=request.POST
        imagen = request.FILES.get("imagen")

        if data["categoria"] != "none":
            categoria_ = Categoria_artista.objects.get(id=data["categoria"])
        else:
            categoria_ = None

    
        artista = Artista.objects.create(
            categoria = categoria_,
            nombre = data["nombre"],
            apellido = data["apellido"],
            edad = data["edad"],
            descripcion = data["descripcion"],
            imagen = imagen,
        )
        return redirect('galeria')

    

    return render(request, "agregar_artista.html",context)


def agregar_obra(request):
    categoria_artista = Categoria_artista.objects.all()
    lista_artista = Artista.objects.all()
    lista_galeria = Galeria.objects.all()
    context = {"categoria_artista": categoria_artista,"lista_artista": lista_artista,"lista_galeria":lista_galeria}
    
    if request.method == "POST":
        data=request.POST
        imagen = request.FILES.get("imagen")

    
        obra = Obra.objects.create(
            nombre = data["nombre"],
            imagen = imagen,
            ano = data["ano"],
            tipo_de_artista = Categoria_artista.objects.get(id=data["tipo_de_artista"]) ,
            artista = Artista.objects.get(id=data["artista"]) ,
            precio = data["precio"],
            vendido =data["vendido"] ,
        )
        return redirect('galeria')

    


    return render(request, "agregar_obra.html",context)


















def detalle_artista(request, pk):
    artista  = Artista.objects.get(id=pk)
           
    return render(request, "detalle_artista.html", {"artista": artista})
