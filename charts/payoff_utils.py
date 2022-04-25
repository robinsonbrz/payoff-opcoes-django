

# calcula o payoff de call ou put para determinado valor de cotação
# # e multiplica pela quantidade
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


# Cria uma lista de valores em um range com passos definidos
# Exemplo de 5 até 50 em passos de 0,25
def cria_lista_valores_cotacao(range_min, range_max, steps):
    lista_valores_cotacao = []
    for i in range(range_min, range_max, steps):
        lista_valores_cotacao.append(round((i/100), 2))
    return lista_valores_cotacao


# alimenta uma lista com os possíveis valores de payoff em um range
def cria_lista_valores_payoff(range_min, range_max, steps, call_ou_put, strike, quantidade): # noqa e501
    lista_valores_payoff = []
    for i in range(range_min, range_max, steps):
        lista_valores_payoff.append(calcula_payoff(call_ou_put, strike, i/100, quantidade)) # noqa e501
    return lista_valores_payoff


# concatena duas listas de strings
def concatena_string_listas(lista1, lista2):
    lista_concatenada = []
    for idx, value in enumerate(lista1):
        lista_concatenada.append(str(lista1[idx]) + "   " + str(lista2[idx]) + "%") # noqa e501
    return lista_concatenada
