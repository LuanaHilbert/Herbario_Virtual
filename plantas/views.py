from django.shortcuts import render
from django.http import HttpResponse

def pagina_plantas(request):
    return render(request, 'plantas.html')

def angiospermas(request):
    return render(request, 'angiospermas.html')

def mostra_moveis(request):
    return render(request, 'moveis.html')