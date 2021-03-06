from fileinput import close
from functools import cache
from sre_constants import _NamedIntConstant
from time import sleep

def leitorlinha(linhaA):
    linhaB = []
    aux = []
    
    for c in linhaA:
        if c == " " or c == "\n":
            linhaB.append("".join(aux))
            aux = []
        else:
            aux.append(c)
    linhaB.append("".join(aux))
    return linhaB


#verifica se o estado está presente no o arquivo
def existeEstado(n, nomeArquivo):
    f = open(nomeArquivo, "r")
    for linhaA in f:
        linha = leitorlinha(linhaA)
        if n == int(linha[0]):
            return True
    return False
#ordena os estados da maquina usada pelo usuario
def formataEntrada(nomeArquivo):
    entrada = open("arquivos/entrada.in", "w")
    n = 0
    while True:
        arquivo = open(nomeArquivo, "r")
        for linhaA in arquivo:
            linha = leitorlinha(linhaA)
            if n == int(linha[0]):
                entrada.write(linha[0] + " " + linha[1] + " " + linha[2] + " " + linha[3] + " " + linha[4]+ "\n")
        arquivo.close()
        n += 1
        if not existeEstado(n, nomeArquivo):
            entrada.close()
            break
#verifica tds os simbolos presetes na maquina
def listaSimbolos():
    f = open("arquivos/entrada.in", "r")
    vet = []
    for linhaA in f:
        linha = leitorlinha(linhaA)
        if linha[1] not in vet:
            vet.append(linha[1])
        if linha[2] not in vet:
            vet.append(linha[2])
    #vet.remove('_')
    return vet
# cria uma cabeça q simula uma maquina semi ifinita para a esquerda
def criaCabeca():
    saida = open("arquivos/saida.out", "w")
    entrada = open("arquivos/entrada.in", "r")
    ''' 0 0 0 l 0
        0 1 1 l 0
        0 _ # r 1'''
    saida.write("0 0 0 l 0\n")
    saida.write("0 1 1 l 0\n")
    saida.write("0 _ # r 1\n")
    for linhaA in entrada:
        linha = leitorlinha(linhaA)
        try:#tenta converter em int se não for convertido significa que é um estado não numerico
            saida.write(str(int(linha[0])+1))
        except:
            saida.write(linha[0])
        
        saida.write(" " + linha[1] + " " + linha[2] + " " + linha[3] + " ")

        try:
            saida.write(str(int(linha[4])+1)+ "\n")
        except:
            saida.write(linha[4] + "\n")
    saida.close()
    entrada.close()

#conta numro estados da saida
def contaEstados(arquivo):
    f = open(arquivo, "r")
    maior = 0
    for linhaA in f:
        linha = leitorlinha(linhaA)
        if maior < int(linha[0]):
            maior =  int(linha[0])
    return maior

def copiaSaidaTemp():
    saida = open("arquivos/saida.out", "r")
    temp = open("arquivos/temp.out", "w")
    for linha in saida:
        temp.write(linha)

def copiaTempSaida():
    saida = open("arquivos/saida.out", "w")
    temp = open("arquivos/temp.out", "r")
    for linha in temp:
        saida.write(linha)

def traduz():
    criaCabeca()
    nEstados = contaEstados("arquivos/temp.out")
    listaS = listaSimbolos()
    nsimbolos = len(listaS)

    saida = open("arquivos/saida.out", "w")
    temp = open("arquivos/temp.out", "r")
    for linha in temp:
        saida.write(linha)

    for i in range(nEstados):
        if i == 0: #estado zero serve apenas para definir a cabeca
            continue
        
        nEstados += 1
        saida.write(str(i) + " # # r " + str(nEstados)+ "\n" )
        #estado q aponta e escreve vazio
        for j in range(nsimbolos):
            saida.write(str(nEstados) + " " + listaS[j] + " _ r " + str(nEstados+j+1) + "\n")
        #estados que passam
        for j in range(nsimbolos):
            for k in range(nsimbolos):
                saida.write(str(nEstados+j+1) + " " + listaS[k] + " " + listaS[j] + " r " + str(nEstados+k+1) + "\n")
            saida.write(str(nEstados+j+1) + " _ " + listaS[j] + " l " + str(nEstados+nsimbolos+1) + "\n")
        #estado de retorno
        nEstados += nsimbolos+1
        for j in range(nsimbolos):
            saida.write(str(nEstados) + " " + listaS[j] + " " + listaS[j] + " l " + str(nEstados) + "\n")
        saida.write(str(nEstados) + " # # r " + str(i) + "\n")

    
    saida.close()
    temp.close()

def ClearTemp():
    temp = open("arquivos/temp.out", "w")
    temp.close()
        


nomemaquina = "arquivos/sameamount10.in"
formataEntrada(nomemaquina)
traduz()
ClearTemp()
