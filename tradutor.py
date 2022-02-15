#<current state> <current symbol> <new symbol> <direction> <new state>
#0 _ _ l 1
from fileinput import close
from functools import cache

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
                entrada.write(linha[0] + " " + linha[1] + " " + linha[2] + " " + linha[3] + " " + linha[4]+ "\n")#ver se apagar "" fode td dps
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
    return vet
# cria uma cabeça q simula uma maquina semi ifinita para a direita
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
        try:#tenta converter em int se não for convertido significa que é um estado não numerico ()
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
def contaEstados():
    f = open("arquivos/saida.out", "r")
    maior = 0
    for linhaA in f:
        linha = leitorlinha(linhaA)
        if maior < int(linha[0]):
            maior =  int(linha[0])
    return maior

def regracabeca():
    f = open("arquivos/saida.out", "r")
    f2 = open("arquivos/temp.out", "w")
    e = 0
    nEstados = contaEstados()
    for linhaA in f:
        linha = leitorlinha(linhaA)
        if int(linha[0]) == e:            
            f2.write(linha[0] + " " + linha[1] + " " + linha[2] + " " + linha[3] + " " + linha[4]+ "\n")
        else:
            f2.write(str(e) + " # " + str(e) + " r " + str(nEstados+1) + "\n")
            f2.write(linha[0] + " " + linha[1] + " " + linha[2] + " " + linha[3] + " " + linha[4]+ "\n")
            e += 1
    f2.write(str(e) + " # " + str(e) + " r " + str(nEstados+1) + "\n")
#escrever um codigo para temp sobrescrever saida

def EstadosDeMovimento():
    nestados = contaEstados()
    
            

    


        

        

#f = open("arquivos/sameamount10.in", "r")
nomemaquina = "arquivos/sameamount10.in"
#formataEntrada(nomemaquina)
#criaCabeca()
#regracabeca()
print(listaSimbolos())