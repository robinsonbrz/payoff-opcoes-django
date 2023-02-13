import numpy as np
import pandas as pd
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import charts.payoff_utils as pu
from random import randint


def home(request):
    range_min = 2000
    range_max = 3725
    steps = 25
    preco_referencia = 25.65

    # transformar opções em objetos
    # todo inputs
    # input preço de referência
    # input opção: call ou put;  valor strike;  quantidade; positivo é compra negativo é venda
    # Lista de opções
    # possibilidade de inserir papel
    # possibilidade de modificar o range do payoff
    # possibilidade de modificar os steps do cálculo

    # possibilidade de inserir valor de compra ou venda da opção para a simulação
    # somente com valores de C/V é possível calcular o payoff


    list_label = pu.cria_lista_valores_cotacao(range_min, range_max, steps)
    # list_Payoff_1 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'put', 29.59, -10000) # noqa e501
    # list_Payoff_2 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'call', 33.59, -10000) # noqa e501
    # list_Payoff_3 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'put', 25.09, 10000) # noqa e501
    # list_Payoff_4 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'call', 38.09, 10000) # noqa e501

    list_Payoff_1 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'put', 38.76, 1000) # noqa e501
    list_Payoff_2 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'call', 28.01, -13000) # noqa e501
    list_Payoff_3 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'call', 29.01, 8000) # noqa e501
    list_Payoff_4 = pu.cria_lista_valores_payoff(range_min, range_max, steps, 'ativo', 0, 5000) # noqa e501




    a = np.array(list_Payoff_1)
    b = np.array(list_Payoff_2)


    c = np.array(list_Payoff_3)
    d = np.array(list_Payoff_4)
    vendidas = (a+b+c+d).tolist()
    compradas = [0,]
    # compradas = (c+d).tolist()
    print("compradas", compradas)

    resultante = (a+b+c+d).tolist()

    # calculo do vetor distancia percentual
    dist_percentual = np.array(list_label)



    
    dist_percentual = (((dist_percentual - preco_referencia) / preco_referencia)*100).round(2).tolist() # noqa e501
    lista_concatenada = []
    lista_concatenada = pu.concatena_string_listas(list_label, dist_percentual)

    mydict = {
        'list_label': list_label,
        'vendidas': vendidas,
        'compradas': compradas,
        'resultante': resultante,
        'lista_concatenada': lista_concatenada,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
    }
    return render(request, 'charts/index2.html', context=mydict)
    
    
    # from charts.models import Ativo
    # p = Ativo.objects.all().order_by('-id')[:10] 


class AjaxCalculoHandler(View):
    def get(self, request):
        if request.headers.get('X-Requested-Width') == 'XMLHttpRequest':
            lista_number = [ (randint(0, 999)/100) for _ in range(10)]
            print(lista_number)
            return JsonResponse({'number':lista_number})
