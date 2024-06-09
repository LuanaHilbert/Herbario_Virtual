from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_plantas(request):
    return HttpResponse('Página de Plantas')
