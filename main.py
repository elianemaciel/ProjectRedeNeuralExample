# coding=utf-8

from neuronio import Neuronio
from conexao import Conexao
import random
from math import exp, expm1

taxa_aprendizagem = 0.8
momentum = 1.0

def calcula_saida(camada_esquerda, camada_direita):
    # Calcule a saídas dos neurônios das camadas escondidas

    try:
        pos_dir = 0
        pos_esq = 0
        somatorio = 0.00
        for neuronio in camada_direita:
            somatorio = 0.00
            for neuronio_anterior in camada_esquerda:
                somatorio += neuronio_anterior.update_saida(pos_dir)
                pos_esq += 1

            somatorio = 1/(1 + exp(-somatorio))
            neuronio.set_valor(somatorio)
            pos_dir +=1
            pos_esq = 0
    except Exception as e:
        print("Erro no calculo de saida ", e)


def calcula_erro(camada_intermediaria=None, camada_final=None, ultima_camada=False):

    try:
        if ultima_camada:
            for neuronio in camada_final:
                fatorErro = neuronio.valor_esperado - neuronio.valor
                erro = neuronio.valor * (1 - neuronio.valor) * fatorErro
                neuronio.erro = erro
        else:

            for neuronio in camada_intermediaria:
                i = 0
                fatorErro = 0
                for neuronio_dois in camada_final:
                    fatorErro += neuronio_dois.erro * neuronio.conexoes[i].peso
                    i += 1

                erro = neuronio.valor * (1 - neuronio.valor) * fatorErro
                neuronio.erro = erro
    except Exception as e:
        print("Erro no calculo de erro ", e)



def ajuste_peso(camada_esquerda, camada_direita):
    # import ipdb; ipdb.set_trace()
    try:
        i = 0
        for neuronio in camada_direita:

            for neuronio_dois in camada_esquerda:
                peso = neuronio_dois.update_pesos(
                    pos=i,
                    momentum=momentum,
                    taxa_aprendizagem=taxa_aprendizagem,
                    erro=neuronio.erro
                )
                neuronio_dois.conexoes[i].set_peso(peso)

            i += 1
    except Exception as e:
        print("Erro na função de ajuste de peso", e)


def verifica_resultado(camada_final, matriz_confusao):
    try:
        maior = 0
        pos_maior = 0
        pos_valor_correto = 0
        # import ipdb; ipdb.set_trace()
        for i, neuronio in enumerate(camada_final):
            if(neuronio.valor>maior):
                maior = neuronio.valor
                pos_maior = i

            if(neuronio.valor_esperado == 1):
                pos_valor_correto = i

            # print("Valor Correto: ", pos_valor_correto, " pos_maior: ",pos_maior)

        # print(matriz_confusao[pos_valor_correto][pos_maior])
        matriz_confusao[pos_valor_correto][pos_maior] += 1
    except Exception as e:
        print("Problema na função verifica resultado ", e)
    return matriz_confusao

def entradas(linha, camada_inicial, camada_final):
    #  Leitura Arquivo
    try:
        list_linha = linha.replace(" ", "").replace("\n", "").split(",")

        for i in range(len(list_linha)-1):
            camada_inicial[i].set_valor(float(list_linha[i])/100)	# Normalizando valor para no saturar neurnios

        for neuronio in camada_final:
            neuronio.set_valor_esperado(0)

        #  Insere 1 na posio que identifica o valor esperado
        camada_final[int(list_linha.pop())].set_valor_esperado(1)
    except Exception as e:
        print("Erro ao fazer as entradas "  , e)



def print_dados(matriz_confusao):
    precisao = 0.00
    sensitividade = 0.00
    especificidade= 0.00
    # PRECISO = VP / (VP + FP)
    # SENSITIVIDADE = VP / (VP + FN)
    # ESPECIFICIDADE = VN / (VN + FP)
    VP = 0.00
    VN = 0.00
    FP = 0.00
    FN = 0.00

    # Acurácia = (VP+VN)/(VP+FP+VN+FN)
    # Erro = 1-Acurácia
    # Recall ou Sensitividade=VP/(VP+FN)
    # Precisão=VP/(VP+FP)
    # Especificidade=VN/(VN+FP)
    # Fmeasure=2*(Recall*Precisão)/(Recall+Precisão)
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

                precisao = (VP / (VP + FP))
                sensitividade = VP / (VP + FN)
                especificidade = VN / (VN + FP)

    print("Nmero: " + i)
    # print("VP: " + VP + " VN: " + VN + " FP: " + FP + " FN: "+ FN)
    print("Precisao: " + precisao)
    print("Sensitividade: " + sensitividade)
    print("Especificidade: " + especificidade)
    print()


def mostra_tabela(matriz_confusao):
    for i in range(10):
        for j in range(10):
            print("%d\t" % matriz_confusao[i][j], end="")

        print()


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
    camada1 = [] # ArrayList neuronio
    camada2 = []
    camada3 = []
    i = 0
    j = 0


    for i in range(16):
        camada1.append(Neuronio())

    for i in range(13):
        camada2.append(Neuronio())

    for i in range(10):
        camada3.append(Neuronio())

    peso = 0.0

    for i in range(16):
        for j in range(13):
            peso = random.uniform(0.0, 1.0)
            if (peso == 0.0): # no pode ser exatamente 0
                peso = 0.1
            elif (peso == 1.0): # nem exatamente 1
                peso = 0.90
            camada1[i].conexoes.append(Conexao(peso))

    for i in range(13):
        for j in range(10):
            peso = random.uniform(0.0, 1.0)
            if peso == 0.0: # talvez testar entre 0 e 100
                peso = 0.1
            elif peso == 1.0:
                peso = 0.90
            camada2[i].conexoes.append(Conexao(peso))

    # Fim das inicializaes

    # Aprendizado
    try:

        file_tra = open("pendigits.tra", 'r')

        linha = file_tra.readline()
        cont = 0
        while linha:
            # Passo 1 – As entradas
            # print(linha)
            entradas(linha, camada1, camada3)
            # Passo 2 – Saída da rede
            calcula_saida(camada1,camada2)
            calcula_saida(camada2,camada3)

            # Passo 3 – Cálculo do Erro
            calcula_erro(camada_final=camada3, ultima_camada=True)
            calcula_erro(camada_intermediaria=camada2, camada_final=camada3)

            # Passo 4 – Ajuste dos Pesos
            ajuste_peso(camada1,camada2)
            ajuste_peso(camada2,camada3)

            linha = file_tra.readline()
            # matriz_confusao = verifica_resultado(camada3, matriz_confusao)
            cont += 1
        file_tra.close()

    except Exception as e:
        print('erro ao ler arquivo', e)

    mostra_tabela(matriz_confusao)
    print()

    try:
        # file_tes = open("pendigits.tes", 'r')
        # linha = file_tes.readline()
        # cont = 0

        file_tra = open("pendigits.tra", 'r')

        linha = file_tra.readline()
        for cont in range(1000):
            for i in linha:
                # entradas(linha, camada1, camada3)

                calcula_saida(camada1,camada2)
                calcula_saida(camada2,camada3)

                # Passo 3 – Cálculo do Erro
                calcula_erro(camada_final=camada3, ultima_camada=True)
                calcula_erro(camada_intermediaria=camada2, camada_final=camada3)

                # Passo 4 – Ajuste dos Pesos
                ajuste_peso(camada1,camada2)
                ajuste_peso(camada2,camada3)


                matriz_confusao = verifica_resultado(camada3, matriz_confusao)

                linha = file_tra.readline()
            print()
            mostra_tabela(matriz_confusao)
    except Exception as e:
        print("Erro Leitura arquivo pendigits.tes ", e)



    # print_dados(matriz_confusao);


main()
