def retirar_letras_unicas(sequencia):
    letra_anterior = sequencia[0]
    string_sequencia = ""
    #Comparador pra ver se o primeiro é igual o segundo
    if sequencia[0] != sequencia[1]:
        letra_anterior = sequencia[1]
    lista_sequencias = []
    #for que compara a anterior com a atual
    for c in sequencia:
        if letra_anterior == c:
            letra_anterior = c
            string_sequencia += c
        else:
            if len(string_sequencia) > 1:
                lista_sequencias.append(string_sequencia)
            string_sequencia = c
            letra_anterior = c
    sequencia_hash = {}
    for i in range(len(lista_sequencias)):
        sequencia_hash[i] = lista_sequencias[i]
    #se a sequencia for de apenas uma string e ela for maior que 10
    if len(string_sequencia) > 9 and lista_sequencias == []:
        sequencia_hash[0] = string_sequencia
    return sequencia_hash

def formar_sublistas(sequencia_hash):
    lista_final = []
    if len(sequencia_hash) > 1:
        for i in range(len(sequencia_hash)):
            soma = len(sequencia_hash[i])
            string_soma = sequencia_hash[i]
            for j in range(i+1, len(sequencia_hash)):
                if soma == 10:
                    break
                if soma + len(sequencia_hash[j]) <= 10:
                    soma += len(sequencia_hash[j])
                    string_soma += sequencia_hash[j]
            if len(string_soma) == 10:
                lista_final.append((string_soma))
    else:
        string_unica = sequencia_hash[0]
        if len(string_unica) >= 10:
            lista_final.append(string_unica[:10])
    return(lista_final)

def menu(sequencia):
    sequencia_seprada = retirar_letras_unicas(sequencia)
    print(formar_sublistas(sequencia_seprada))

menu("AAAAACCCCCAAAAGGGGCCTTTTG")
menu("AAAAAAAAAAAAA")