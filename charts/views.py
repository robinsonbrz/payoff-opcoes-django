import numpy as np
import pandas as pd
from django.shortcuts import render

# from .models import Student


def calcula_payoff(call_ou_put, strike, cotacao, quantidade):
    if call_ou_put == 'call':
        if strike > cotacao:
            return 0.00
        else:
            return round(((strike)-(cotacao)) * -quantidade, 2)
    if call_ou_put == 'put':
        if strike < cotacao:
            return 0.00
        else:
            return round(((cotacao)-(strike)) * -quantidade, 2)


def cria_lista_valores_cotacao(range_min, range_max, steps):    
    lista_valores_cotacao = []
    for i in range(range_min, range_max, steps):
        lista_valores_cotacao.append(round((i/100), 2))
    return lista_valores_cotacao


def cria_lista_valores_payoff(range_min, range_max, steps, call_ou_put, strike, cotacoes, quantidade):
    lista_valores_payoff = []
    for i in range(range_min, range_max, steps):
        lista_valores_payoff.append(calcula_payoff(call_ou_put, strike, i/100, quantidade))
    return lista_valores_payoff


def concatena_string_listas(lista1, lista2):
    lista_concatenada = []
    for idx, value in enumerate(lista1):
        lista_concatenada.append(str(lista1[idx]) + "   " + str(lista2[idx]) + "%")
    return lista_concatenada


# Create your views here.
#def home(request):
#    item = Student.objects.all().values()
#    df = pd.DataFrame(item)
#    df1 = df.name.tolist()
#    df = df['rank'].tolist()
#    mydict = {
#        'df': df,
#        'df1': df1,
#    }
#    return render(request, 'charts/index.html', context=mydict)


def home2(request):
    range_min = 400
    range_max = 4325
    steps = 25
    preco_referencia = 31.54
    list_label = cria_lista_valores_cotacao(range_min, range_max, steps)
    list_Payoff_1 = cria_lista_valores_payoff(range_min, range_max, steps, 'put', 29.59, list_label, -10000 )
    list_Payoff_2 = cria_lista_valores_payoff(range_min, range_max, steps, 'call', 33.59, list_label, -10000 )
    list_Payoff_3 = cria_lista_valores_payoff(range_min, range_max, steps, 'put', 25.09, list_label, 10000 )
    list_Payoff_4 = cria_lista_valores_payoff(range_min, range_max, steps, 'call', 38.09, list_label, 10000 )

    a = np.array(list_Payoff_1)
    b = np.array(list_Payoff_2)
    vendidas = (a+b).tolist()

    c = np.array(list_Payoff_3)
    d = np.array(list_Payoff_4)
    compradas = (c+d).tolist()
    
    resultante = (a+b+c+d+13900).tolist()

    # calculo do vetor distancia percentual   
    dist_percentual =  np.array(list_label)

    
    dist_percentual = (((dist_percentual - preco_referencia) / preco_referencia)*100).round(2).tolist() # noqa e501
    lista_concatenada = []
    lista_concatenada = concatena_string_listas(list_label, dist_percentual)

    mydict = {
        'list_label': list_label,
        'vendidas': vendidas,
        'compradas': compradas,
        'resultante': resultante,
        'lista_concatenada': lista_concatenada,
    }
    return render(request, 'charts/index2.html', context=mydict)
    
    
    # from charts.models import Ativo
    # p = Ativo.objects.all().order_by('-id')[:10] 
