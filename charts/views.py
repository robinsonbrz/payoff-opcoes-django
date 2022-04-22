import numpy as np
import pandas as pd
from django.shortcuts import render

from .models import Student


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


# Create your views here.
def home(request):
    item = Student.objects.all().values()
    df = pd.DataFrame(item)
    df1 = df.name.tolist()
    df = df['rank'].tolist()
    mydict = {
        'df': df,
        'df1': df1,
    }
    return render(request, 'charts/index.html', context=mydict)


def home2(request):
    range_min = 2000
    range_max = 4325
    steps = 25
    list_label = cria_lista_valores_cotacao(range_min, range_max, steps)
    list_Payoff_1 = cria_lista_valores_payoff(range_min, range_max, steps, 'put', 29.59, list_label, -10000 )
    list_Payoff_2 = cria_lista_valores_payoff(range_min, range_max, steps, 'call', 33.59, list_label, -10000 )
    list_Payoff_3 = cria_lista_valores_payoff(range_min, range_max, steps, 'put', 25.09, list_label, 10000 )
    list_Payoff_4 = cria_lista_valores_payoff(range_min, range_max, steps, 'call', 38.09, list_label, 10000 )

    a = np.array(list_Payoff_1)
    b = np.array(list_Payoff_2)
    vendidas =  (a+b).tolist()

    c = np.array(list_Payoff_3)
    d = np.array(list_Payoff_4)
    compradas = (c+d).tolist()
    
    resultante = (a+b+c+d+13900).tolist()
    mydict = {
        'list_label': list_label,
        'vendidas': vendidas,
        'compradas': compradas,
        'resultante': resultante,
    }
    return render(request, 'charts/index2.html', context=mydict)
