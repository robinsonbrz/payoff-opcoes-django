from django.contrib import admin

from .models import *


@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('nome_ativo', 'valor_strike', 'vencimento')


@admin.register(Cotacao)
class CotacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_ativo', 'data_hora_cotacao')


@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_ativo', 'quantidade')
