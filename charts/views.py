import numpy as np
import pandas as pd
from django.shortcuts import render

import charts.payoff_utils as pu


def home(request):
    range_min = 400
    range_max = 4325
    steps = 25
    preco_referencia = 31.54
    list_label = pu.cria_lista_valores_cotacao(range_min, range_max, steps)
    list_Payoff_1 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'put', 29.59, -10000) # noqa e501
    list_Payoff_2 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'call', 33.59, -10000) # noqa e501
    list_Payoff_3 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'put', 25.09, 10000) # noqa e501
    list_Payoff_4 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'call', 38.09, 10000) # noqa e501

    a = np.array(list_Payoff_1)
    b = np.array(list_Payoff_2)
    vendidas = (a+b).tolist()

    c = np.array(list_Payoff_3)
    d = np.array(list_Payoff_4)
    compradas = (c+d).tolist()

    resultante = (a+b+c+d+11500).tolist()

    # calculo do vetor distancia percentual
    dist_percentual = np.array(list_label)
    print(a)
    print(b)
    print(c)
    print(d)


    
    dist_percentual = (((dist_percentual - preco_referencia) / preco_referencia)*100).round(2).tolist() # noqa e501
    lista_concatenada = []
    lista_concatenada = pu.concatena_string_listas(list_label, dist_percentual)

    mydict = {
        'list_label': list_label,
        'vendidas': vendidas,
        'compradas': compradas,
        'resultante': resultante,
        'lista_concatenada': lista_concatenada,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
    }
    return render(request, 'charts/index2.html', context=mydict)
    
    
    # from charts.models import Ativo
    # p = Ativo.objects.all().order_by('-id')[:10] 
