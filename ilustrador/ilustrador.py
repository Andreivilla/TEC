#<current state> <current symbol> <new symbol> <direction> <new state>
 #0 _ _ l 1
 # arquivo.write
 #EXISTE UM ERRO NOS TABS
 #CRIAR UM SISTEMA PARA O MOVIMENTO ESTACIONARIO *->state
from ntpath import join
import re
from tkinter.messagebox import RETRY

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

def existeEstado(n):
    f = open("ilustrador/entrada.in", "r")
    for linhaA in f:
        linha = leitorlinha(linhaA)
        print("n: " + str(n) + " linha0: " + linha[0])
        if n == int(linha[0]):
            print("entrou")
            return True
    return False



faux = open("ilustrador/temp.in", "w")

faux.write('''input: '1011'
blank: '_'
start state: Q0
table: \n''')

ordem = 0
while(True):
    print(ordem)
    faux.write("\tQ" + str(ordem) + ":\n")
    f = open("ilustrador/entrada.in", "r")
    for linhaA in f:
        linha = leitorlinha(linhaA)
        if int(linha[0]) == ordem:
            faux.write("\t\t" + linha[1] + ": " "{write: " + linha[2] + ", " + linha[3].upper() + ": Q" + linha[4] + "}\n")
    f.close
    ordem = ordem + 1
    if not existeEstado(ordem):
        break

'''
f = open("ilustrador/entrada.in", "r")
for linha in f:
    print("estado atual: " + linha[0] + " simbolo atual: " + linha[2] + " novo simbolo: " 
            + linha[4]+ " direcao: " + linha[6] + " novo estado: " + linha[8])
'''