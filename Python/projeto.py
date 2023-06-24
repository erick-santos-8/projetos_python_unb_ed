def tolerancia(x):
    x = x.replace(" ", "")
    if x == "-20" or x == "20":
        return "Nenhuma"
    elif x == "-10" or x== "10":
        return "Prata"
    elif x == "5" or x == "-5":
        return "Dourada"
    elif x == "1" or x == "-1":
        return "Marrom"
    elif x == "2" or x == "-2":
        return "Vermelha"
    elif x == "0.05" or x == "-0.05":
        return "Laranja"
    elif x == "0.02" or x == "-0.02":
        return "Amarela"
    elif x == "0.5" or x == "-0.5":
        return "Verde"
    elif x == "0.25" or x == "-0.25":
        return "Azul"
    elif x == "0.1" or x == "-0.1":
        return "Violeta"
    elif x == "0.01" or x == "-0.01":
        return "Cinza"


def dicMultSub(ref):
    if ref == "-2":
        return "Prata"
    elif ref == "-1":
        return "Dourada"
    
def dicSignificativo(x):
    if x == "0":
        return "Preta"
    elif x == "1":
        return "Marrom"
    elif x == "2":
        return "Vermelha"
    elif x == "3":
        return "Laranja"
    elif x == "4":
        return "Amarela"
    elif x == "5":
        return "Verde"
    elif x == "6":
        return "Azul"
    elif x == "7":
        return "Violeta"
    elif x == "8":
        return "Cinza"
    elif x == "9":
        return "Branca"
    
def dicMult(x, n):
    ref = ""
    numM = 0
    if n == 0:
        if x == "m":
            return "Rosa"
        elif x == "-":
            return "Preta"
        elif x == "K":
            return "Laranja"
        elif x == "M":
            return "Azul"
        elif x == "G":
            return "Branca"
    else:
        if x == "m":
            return "Rosa"
        elif x == "K":
            numM = 3
        elif x == "M":
            numM = 6
        elif x == "G":
            numM = 9
        numM = numM-n
        ref = str(numM)
        if numM>-1:
            ref = dicSignificativo(ref)
            return ref
        elif numM<-2:
            return "Rosa"
        else:
            ref = dicMultSub(ref)
            return ref
        
def ponto(x):
    pon = False
    cont = 0
    x = x.replace(" ", "")
    for i in range(len(x)):
        if pon == True:
            cont+=1
        if x[i] == ".":
            pon = True
    return cont

def defMult(x, numeroL):
    lista = []
    ref = ""
    qtdN = ponto(x[:len(x)-1])
    if qtdN>0:
        x = x.replace(".", "")
    for i in range(len(x)-1):
        ref = dicSignificativo(x[i])
        lista.append(ref)
    ref = dicMult(x[len(x)-1], qtdN)
    lista.append(ref)
    if numeroL<2:
        lista.append("Dourada")
    return lista
    
def IEC60062(x):
    lista = []
    mult = 0
    if x.find("m") > -1:
        mult = x.find("m")
    elif x.find("-") > -1:
        mult = x.find("-")
    elif x.find("K") > -1:
        mult = x.find("K")
    elif x.find("M") > -1:
        mult = x.find("M")
    elif x.find("G") > -1:
        mult = x.find("G")
    xAteMult = x[:(mult+1)]
    lista = defMult(xAteMult, mult)
    lista.append(tolerancia(x[mult+1:]))
    return lista
print(IEC60062('1- 10'))
print(IEC60062('2.70M 0.01'))
print(IEC60062('13m 0.02'))
print(IEC60062('2.26K 0.05'))
print(IEC60062('2.7M 1'))
print(IEC60062('2.2K 2'))
print(IEC60062('10000K 20'))