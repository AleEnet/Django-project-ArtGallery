from django.shortcuts import render, redirect
from .models import  *


def galeria(request):
    categoria = request.GET.get("categoria")
    tipo_artista = request.GET.get("tipo_artista")
    categorias_proyectos= Categoria_proyecto.objects.all()
    
    

    if categoria == None or categoria == "Artistas":
        elementos = Categoria_artista.objects.all()
        filtro = 0
        if tipo_artista != None:
            categoria_artista = Categoria_artista.objects.get(nombre=tipo_artista)
            elementos = Artista.objects.filter(categoria = categoria_artista)
            filtro = 3

        
    elif categoria == "Obras":
        elementos = Obra.objects.all()
        filtro = 1
    
    else:
        elementos = Galeria.objects.all()
        filtro = 2
        
    


    context = {"categorias_proyectos" : categorias_proyectos, "elementos" : elementos,"filtro": filtro}
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


def agregar_galeria(request):
    
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("imagen")
    
        galeria = Galeria.objects.create(
            nombre = data["nombre"],
            direccion = data["direccion"],
            imagen = image
        )
        return redirect('galeria')

    return render(request,"agregar_galeria.html")




def buscar(request):

    categoria = request.GET.get("categoria")
    categorias_proyectos= Categoria_proyecto.objects.all()
    
    if categoria == None or categoria == "Artistas":
        elementos = Categoria_artista.objects.all()
        filtro = 0
        
        
    elif categoria == "Obras":
        elementos = Obra.objects.all()
        filtro = 1
    
    else:
        elementos = Galeria.objects.all()
        filtro = 2
  
 
    if request.method == "POST":
        busqueda = request.POST["busqueda"]
        lista_artistas = Artista.objects.filter(apellido__contains = busqueda)
        lista_obras = Obra.objects.filter(nombre__contains = busqueda)
        lista_galeria = Galeria.objects.filter(nombre__contains = busqueda)

        return render (request,"buscar.html", {"busqueda":busqueda,
         "lista_artistas":lista_artistas,
         "lista_obras": lista_obras,
         "lista_galerias":lista_galeria,
         "categorias_proyectos" : categorias_proyectos,
          "elementos" : elementos,
          "filtro": filtro })

   