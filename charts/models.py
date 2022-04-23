from django.db import models

# Create your models here.
# class Student(models.Model):
#    name = models.CharField(max_length=200)
#    rank = models.IntegerField()


class Ativo(models.Model):
    nome_ativo = models.CharField(max_length=10)
    valor_strike = models.FloatField()
    vencimento = models.DateField()
    am_europeia = models.CharField(max_length=2)
    on_pn = models.CharField(max_length=2, default="PN")
    call_put_papel = models.CharField(max_length=2)
    formador_mercado = models.CharField(max_length=2, default="", blank=True)
    empresa = models.CharField(max_length=18, default="Petrobras")
    data_criacao_tabela = models.DateTimeField()
    habilitado = models.BooleanField(default="true")

    def __str__(self):
        return f"{self.nome_ativo}  {self.valor_strike}  {self.vencimento}"


class Cotacao(models.Model):
    valor_bid = models.FloatField()
    valor_ask = models.FloatField()
    data_hora_cotacao = models.DateTimeField()
    valor_cotacao_papel_instante = models.FloatField()
    nome_ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_ativo}  {self.valor_bid}  {self.valor_ask}"


class Operacao(models.Model):
    quantidade = models.IntegerField()
    valor_total = models.FloatField()
    cotacao = models.ForeignKey(Cotacao, on_delete=models.CASCADE)
    nome_ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantidade}  {self.cotacao.valor_bid}  {self.cotacao.valor_ask}" # noqa e502
