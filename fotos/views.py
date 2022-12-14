from django.shortcuts import render


def galeria(request):
    return render(request, "galeria.html")


def agregar_artista(request):
    return render(request, "agregar_artista.html")


def detalle_artista(request, pk):
    return render(request, "detalle_artista.html")
