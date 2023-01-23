import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def calcular_aliquota_ir(days):
    if days <= 180:
        return 0.225
    elif days <= 360:
        return 0.2
    elif days <= 720:
        return 0.175
    else:
        return 0.15


def calcular_iof_regressivo(days):
    return max((100 - (days * 3 + math.ceil((float(days) / 3)))), 0) / 100


class RendaFixa:
    def __init__(
        self,
        capital_inicial=1.0,
        rendimento_mensal=0.0,
        data_aplicacao=None,
        isento_ir=False,
        isento_iof=False,
    ):
        self.capital_inicial = capital_inicial
        self.rendimento_mensal = rendimento_mensal
        self.data_aplicacao = data_aplicacao
        self.isento_ir = isento_ir
        self.isento_iof = isento_iof

    def simular(self, months=None):
        valor_bruto = self.capital_inicial * (1 + self.rendimento_mensal) ** months

        rendimento = valor_bruto - self.capital_inicial

        valor_liquido = valor_bruto
        if not self.isento_ir:
            valor_liquido -= rendimento * calcular_aliquota_ir(months * 30)
        if not self.isento_iof:
            valor_liquido -= rendimento * calcular_iof_regressivo(months * 30)
        return valor_liquido


#r = RendaFixa(capital_inicial=100000, rendimento_mensal=0.0081, isento_ir=False, isento_iof=False)
#r.simular(12)
