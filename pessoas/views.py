from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    idade = 18
    tipo=''
    if idade < 12:
        tipo = "Criança"
    elif idade >= 12 and idade <= 18:
        tipo = "Adolescente"
    else:
        tipo = "Adulto"

    context = {
        'ultimo_acesso':'2024-06-10',
        'idade':15,
        'tipo':tipo,
        'clientes':[
            {'nome':'Luana Hilbert','qtde_reg':'10'},
            {'nome':'Lucas Medinaa', 'qtde_reg':'2'},
            {'nome': 'Eric Cartman', 'qtde_reg': '1'},

        ]

    }

    return render(request, 'index.html', context)

