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

    def __str__(self):
        return "Valor: {valor}, valor esperado: {valor_esperado} , erro: {erro}".format(
            valor=self.valor, valor_esperado=self.valor_esperado, erro=self.erro)

    def getConexoes(self, i):

        return conexoes[i]

    def soma_valor(self, valor):

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

    def set_erro(self, erro):
        self.erro = erro

    def print_conexoes(self):
        for conexao in self.conexoes:
            print(conexao)
