from django.shortcuts import render


def productos(request):
    return render(request, 'tienda/productos.html')


def ofertas(request):
    return render(request, 'tienda/ofertas.html')
