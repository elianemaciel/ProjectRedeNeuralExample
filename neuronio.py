# coding=utf-8

class Neuronio():
    valor = 0.0
    erro = 0.0
    valor_esperado = 0
    conexoes = []

    def __init__(self, valor=0.00, erro=0, valor_esperado=0,conexoes=[]):
        self.valor = valor
        self.erro = erro
        self.valor_esperado = valor_esperado
        self.conexoes = conexoes

    def getConexoes(self, i):

        return conexoes[i]

    def somaValor(self, valor):

        self.valor += valor

    def funcao_rigida(self, somatorio=0):
        if (somatorio<0.5):
            saida = 0
        else:
            saida = 1
        return saida

    def set_valor(self, valor):
        self.valor = valor

    def set_valor_esperado(self, valor):
        self.valor_esperado = valor

    def update_saida(self, pos=0):
        return  self.conexoes[pos].peso * self.valor

    def update_pesos(self, pos=0, momentum=1.0, taxa_aprendizagem=0.8, erro=0):
        peso = self.conexoes[pos].peso * momentum+ taxa_aprendizagem * self.valor * erro
        return peso
