# coding=utf-8

from neuronio import Neuronio
from conexao import Conexao
import random
from math import exp, expm1
import random
import numpy as np

TAXA_APRENDIZAGEM = 0.9
momentum = 1.0

def funcao_rigida(somatorio):
    if somatorio < 0.5:
        return 0
    else:
        return 1

def funcao_sigmoidal(somatorio):
    valor = 1.0  / (1.0 + exp(-somatorio))
    print(valor)
    return valor


def calcula_saida(camada_esquerda, camada_direita, teste=False):
    # Calcule a saídas dos neurônios das camadas escondidas

    try:
        somatorio = 0.00
        for neuronio in camada_direita:
            somatorio = 0.00
            for neuronio_anterior in camada_esquerda:
                pos = camada_direita.index(neuronio)
                somatorio += neuronio_anterior.conexoes[pos].peso * neuronio_anterior.valor
            somatorio = funcao_sigmoidal(somatorio)
            neuronio.set_valor(somatorio)

    except Exception as e:
        print("Erro no calculo de saida ", e)


def calcula_erro(camada_intermediaria=None, camada_final=None, ultima_camada=False):

    try:
        if ultima_camada:
            for neuronio in camada_final:
                fator_erro = neuronio.valor_esperado - neuronio.valor
                erro = neuronio.valor * (1 - neuronio.valor) * fator_erro
                neuronio.set_erro(erro)
        else:
            for neuronio in camada_intermediaria:
                fator_erro = 0.00
                for i, neuronio_final in enumerate(camada_final):
                    fator_erro += neuronio_final.erro * neuronio.conexoes[i].peso
                erro = neuronio.valor * (1.0 - neuronio.valor) * fator_erro
                neuronio.set_erro(erro)
    except Exception as e:
        print("Erro no calculo de erro ", e)


def update_pesos(neuronio, pos=0, taxa_aprendizagem=0.8, erro=0):
    peso = neuronio.conexoes[pos].peso + taxa_aprendizagem * neuronio.valor * erro
    return peso

def ajuste_peso(camada_esquerda, camada_direita):
    # import ipdb; ipdb.set_trace()
    try:
        for i, neuronio in enumerate(camada_direita):
            for neuronio_dois in camada_esquerda:
                peso = update_pesos(
                    neuronio_dois,
                    pos=i,
                    taxa_aprendizagem=TAXA_APRENDIZAGEM,
                    erro=neuronio.erro
                )
                neuronio_dois.conexoes[i].set_peso(peso)

    except Exception as e:
        print("Erro na função de ajuste de peso", e)


def verifica_resultado(camada_final, matriz_confusao):
    try:
        maior = 0
        pos_maior = 0
        pos_valor_correto = 0
        for i, neuronio in enumerate(camada_final):
            if(neuronio.valor>maior):
                maior = neuronio.valor
                pos_maior = i

            if(neuronio.valor_esperado == 1):
                pos_valor_correto = i

        matriz_confusao[pos_maior][pos_valor_correto] += 1
        # print(matriz_confusao)
    except Exception as e:
        print("Problema na função verifica resultado ", e)
    return matriz_confusao

def entradas(linha, camada_inicial, camada_final, teste=False):
    #  Leitura Arquivo
    try:

        for i, value in enumerate(linha):
            if i == len(linha)-1:
                break

            camada_inicial[i].set_valor(float(value))

        for neuronio in camada_final:
            neuronio.set_valor_esperado(0)
            if teste:
                neuronio.set_valor(0)

        #  Insere 1 na posio que identifica o valor esperado
        camada_final[int(linha.pop())].set_valor_esperado(1)
    except Exception as e:
        print("Erro ao fazer as entradas "  , e)



def calculo_metricas(matriz_confusao):
    VP = 0.00
    VN = 0.00
    FP = 0.00
    FN = 0.00

    acuracia = 0.00
    erro = 0.00
    sensitividade = 0.00
    precisao = 0.00
    especificidade = 0.00
    fmeasure = 0.00
    for i in range(10):
        FP = 0.00
        VN = 0.00
        FN = 0.00
        VP = matriz_confusao[i][i]
        for j in range(10):
            if(i!=j):
                FP += matriz_confusao[j][i]
                FN += matriz_confusao[i][j]
                VN += matriz_confusao[j][j]

    try:
        acuracia = (VP + VN) / (VP + FP + VN + FN)
        erro = 1 - acuracia
        sensitividade = VP / (VP + FN)
        precisao = VP / (VP + FP)
        especificidade = VN / (VN + FP)
        fmeasure = 2 * (sensitividade * precisao) / (sensitividade + Precisao)

        print("Número: ", i)
        print("VP: ", VP, " VN: ", VN, " FP: ", FP, " FN: ", FN)
        print("Precisao: ", precisao)
        print("Sensitividade: ", sensitividade)
        print("Especificidade: ", especificidade)
        print("\n")
    except Exception as e:
        print("Problema ao calcular métricas da rede ", e)


def mostra_tabela(matriz_confusao):
    for i in range(10):
        for j in range(10):
            print("%d\t" % matriz_confusao[i][j], end="")

        print()

def inicialize_camada(camada, integer):
    for i in range(integer):
        camada.append(Neuronio())
    return camada

def append_conexoes(camada, num):
    peso = 0.0
    for neuronio in camada:
        for j in range(num):
            peso = round(random.uniform(0.0, 1.0), 3)
            if (peso == 0.0): # no pode ser exatamente 0
                peso = 0.1
            elif (peso == 1.0): # nem exatamente 1
                peso = 0.90
            neuronio.conexoes.append(Conexao(peso))

def treinamento(camada1, camada2, camada3):
    # Passo 2 – Saída da rede
    calcula_saida(camada1,camada2)
    calcula_saida(camada2,camada3)

    # # Passo 3 – Cálculo do Erro
    calcula_erro(camada_final=camada3, ultima_camada=True)
    calcula_erro(camada_intermediaria=camada2, camada_final=camada3)

    # # Passo 4 – Ajuste dos Pesos
    ajuste_peso(camada2,camada3)
    ajuste_peso(camada1,camada2)


def main():
    matriz_confusao = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    camada1 = inicialize_camada([], 16)
    camada2 = inicialize_camada([], 13)
    camada3 = inicialize_camada([], 10)

    peso = 0.0

    append_conexoes(camada1, 13)
    append_conexoes(camada2, 10)

    # Fim das inicializacoes
    print("Inicializações com pesos realisadas")
    print("Iniciando o aprendizado")

    # Aprendizado
    try:

        file_tra = open("pendigits.tra", 'r')

        linha = file_tra.readline()
        cont = 0
        while linha:
            # Passo 1 – As entradas
            list_linha = linha.replace(" ", "").replace("\n", "").split(",")
            entradas(list_linha, camada1, camada3)

            # Passo 2 – Saída da rede
            calcula_saida(camada1,camada2)
            calcula_saida(camada2,camada3)

            # # Passo 3 – Cálculo do Erro
            calcula_erro(camada_final=camada3, ultima_camada=True)
            calcula_erro(camada_intermediaria=camada2, camada_final=camada3)

            # # Passo 4 – Ajuste dos Pesos
            ajuste_peso(camada2,camada3)
            ajuste_peso(camada1,camada2)

            linha = file_tra.readline()
            cont += 1
        file_tra.close()
        for i in range(1000):
            treinamento(camada1, camada2, camada3)

    except Exception as e:
        print('erro ao ler arquivo', e)

    print("Fim do Aprendizado")

    try:
        file_tes = open("pendigits.tes", 'r')
        linha = file_tes.readline()
        cont = 0
        while linha:
            list_linha = linha.replace(" ", "").replace("\n", "").split(",")
            entradas(list_linha, camada1, camada3, teste=True)


            calcula_saida(camada1,camada2)

            calcula_saida(camada2,camada3)
            verifica_resultado(camada3, matriz_confusao)

            linha = file_tes.readline()
        file_tes.close()
        print()

    except Exception as e:
        print("Erro Leitura arquivo pendigits.tes ", e)


    mostra_tabela(matriz_confusao)
    calculo_metricas(matriz_confusao)


main()
