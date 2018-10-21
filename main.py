
from neuronio import Neuronio
from conexao import Conexao

taxa_aprendizagem = 0.8
momentum = 1.0
# BufferedReader br

def calculaCamadas(camada_esquerda, camada_direita): # i e j so os tamanhos das camadas
    """
    int tam1,tam2
    tam1 = camada_esquerda.size()
    tam2 = camada_direita.size()
    for (int i = 0 i < tam1 i++)
    {
    for (int j = 0 j < tam2 j++)
    {
    camada_direita.get(j).somaValor(camada_esquerda.get(i).getConexoes(j).getPeso() * camada_esquerda.get(i).getValor())

    # Clculo da Sigmoidal
    camada_direita.get(j).setValor(1 / (1 + (float)Math.exp(-camada_direita.get(j).getValor())))



    """
    posDir = 0
    posEsq = 0
    somatorio = 0.00
    for neuronio in camada_direita:
        somatorio = 0
        for neuronioAnterior in camada_esquerda:
            somatorio += neuronioAnterior.getConexoes(posDir).getPeso() * neuronioAnterior.getValor()
            posEsq +=1

    # somatorio = 1/(1 + (float)Math.exp(-somatorio))
    neuronio.setValor(somatorio)
    posDir +=1
    posEsq = 0



def calculaErro(camada_final):
    for neuronio in camada_final:
        fatorErro = neuronio.getValorEsperado() - neuronio.getValor()
        erro = neuronio.getValor() * (1 - neuronio.getValor()) * fatorErro
        neuronio.setErro(erro)



def calculaErro(camada_intermediaria, camada_final):
    for neuronio in camada_intermediaria:
        i = 0
        fatorErro = 0
    for neuronio_dois in camada_final:
        fatorErro += neuronioFinal.getErro() * neuronioIntermediario.getConexoes(i).getPeso()
        i +=1

    erro = neuronioIntermediario.getValor() * (1 - neuronioIntermediario.getValor()) * fatorErro
    neuronioIntermediario.setErro(erro)



def atualizaPeso(camada_esquerda, camada_direita):
    i = 0
    for neuronio in camada_direita:

        for neuronio_dois in camada_esquerda:
            peso = neuronioAnterior.getConexoes(i).getPeso() * momentum + taxa_aprendizagem * neuronioAnterior.getValor() * neuronio.getErro()
            neuronioAnterior.getConexoes(i).setPeso(peso)

    i += 1



def verificaResultado(camada_final, matriz_confusao):
    maior = 0
    posMaior = 0
    cont = 0
    posValorCorreto = 0
    for neuronio in camada_final:
        if(neuronio.getValor()>maior):
            maior = neuronio.getValor()
            posMaior = cont

    if(neuronio.getValorEsperado() == 1):
        posValorCorreto = cont

    cont += 1
    # print("Valor Correto:" + posValorCorreto + "posMaior:" + posMaior)

    matriz_confusao[posValorCorreto][posMaior] += 1

def lerLinha(linha, camada_inicial, camada_final):
    #  Leitura Arquivo

    s = linha.split(",")

    # for (int i = 0 i < s.length - 1 i++)
    # 	  :
    #
    # 			camada_inicial.get(i).setValor(Float.parseFloat(s[i].trim())/100)	# Normalizando valor para no saturar neurnios
    #
    # 	   for(Neuronio n:camada_final)
    # 	  :
    # 		   n.setValorEsperado(0)
    #
    # 	   #  Insere 1 na posio que identifica o valor esperado
    # 	   camada_final.get(Integer.parseInt(s[s.length-1].trim())).setValorEsperado(1)



def printaDados(matriz_confusao):
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

def printaCoisas(camada1, camada2, camada3):


    print("Resultado Camada 1:")
    for n in camada1:
        print(n.getValor() + " " + n.getValorEsperado())


    print("Conexes Neurnio 1:")
    primeiro = camada1[0]
    for conexao in primeiro.getConexoes():
        print(conexao.getPeso())


    print("Resultado Camada 2:")
    for n in camada2:
        print(n.getValor() + " " + n.getValorEsperado())


    print("Conexes Neurnio C2:")
    primeiroC2 = camada2.get(0)
    for conexao in primeiroC2.getConexoes():
        print(conexao.getPeso())


    print("Resultado Camada 3:")
    for n in camada3:
        print(n.getValor() + " " + n.getValorEsperado())


def mostraTabela(matriz_confusao):
    for i in range(10):
        for j in range(10):
            print(matriz_confusao[i][j], "\t")

        print()

    print()

def main():
    matriz_confusao = [[]]
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

    # Random r = new Random()
    peso = 0.0

    for i in range(16):
        for j in range(13):
            # peso = r.nextFloat()
            if (peso == 0.0): # no pode ser exatamente 0
                peso = 0.1
            elif (peso == 1.0): # nem exatamente 1
                peso = 0.90
            camada1.get(i).getConexoes().add(Conexao(peso))

    for i in range(13):
        for j in range(10):
            peso = r.nextFloat()
            if (peso == 0.0): # talvez testar entre 0 e 100
                peso = 0.1
            elif (peso == 1.0):
                peso = 0.90
                camada2.get(i).getConexoes().add(Conexao(peso))

    # Fim das inicializaes

    # Aprendizado
    try:
        # br = new BufferedReader(new FileReader("./pendigits.tra"))
        linha = br.readLine()
        cont = 0
        while (linha != null):

            lerLinha(linha,camada1, camada3)

            calculaCamadas(camada1,camada2)
            calculaCamadas(camada2,camada3)

            calculaErro(camada3)
            calculaErro(camada2,camada3)

            atualizaPeso(camada1,camada2)
            atualizaPeso(camada2,camada3)

    # falta conferir se o resultado da ltima camada  o resultado esperado
    # precisa usar todos os neurnios da camada, no s o que  igual a 1

    # falta mensagens, tabela de acerto e iteraes sem aprendizado para usar com arq de teste

        # print("Linha" + cont)

        # printaCoisas()
        """print("Resultado Camada 3:")
        for(Neuronio n:camada3)
        {
        print(n.getValor() + " " + n.getValorEsperado())
        """



        cont += 1
        linha = br.readLine()

    except:
        print("Traceback")



    # try:
    #     br = new BufferedReader(new FileReader("./pendigits.tes"))
    #     String linha = br.readLine()
    #     int cont = 0
    #     while (linha != null):
    #
    #         lerLinha(linha,camada1, camada3)
    #
    #         calculaCamadas(camada1,camada2)
    #         calculaCamadas(camada2,camada3)
    #
    #
    #         verificaResultado(camada3, matriz_confusao)
    #
    #
    #
    #         cont++
    #             linha = br.readLine()
    #
    #     catch(IOException e)
    # e.printStackTrace()
    #
    # mostraTabela(matriz_confusao)
    #
    # printaDados(matriz_confusao)

main()
