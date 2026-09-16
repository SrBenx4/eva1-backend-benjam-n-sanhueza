from django.shortcuts import render


def inicio(request):
    return render(request, 'noticias/inicio.html')


def contacto(request):
    return render(request, 'noticias/contacto.html')
