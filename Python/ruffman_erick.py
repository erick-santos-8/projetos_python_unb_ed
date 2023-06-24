
class No:
    def __init__(self, valor, frequencia):
        self.valor = valor
        self.frequencia = frequencia
        self.no_esquerdo = None
        self.no_direito = None
        
    def add_No_esquerdo(self, no_esq):
        self.no_esquerdo = no_esq
        
    def add_No_direito(self, no_dir):
        self.no_direito = no_dir
        
    def __lt__(self, outro_item):
        return self.frequencia < outro_item.frquencia
    
class Arvore_Huffman:
    def __init__(self, no_Raiz):
        self.no_Raiz = no_Raiz
        self.codigo = {}
    
    def construir_arvore(self, frequencias):
        fila_freq = list(frequencias.items())

        while len(fila_freq) > 1:
            fila_freq = sorted(fila_freq, key=lambda x: x[1])
            valor_esquerdo, freq_esquerdo = fila_freq.pop(0)
            valor_direito, freq_direito = fila_freq.pop(0)

            no_esquerdo_loop = No(valor_esquerdo, freq_esquerdo)
            no_direito_loop = No(valor_direito, freq_direito)

            no_pai = No(None, freq_esquerdo + freq_direito)
            no_pai.add_No_esquerdo(no_esquerdo_loop)
            no_pai.add_No_direito(no_direito_loop)

            fila_freq.append((None, freq_esquerdo + freq_direito))

            self.no_Raiz = no_pai

        self.no_Raiz = fila_freq[0][0]

    def gerar_codigos(self, no_atual, codigo_atual):
        if no_atual.valor:
            self.codigo[no_atual.valor] = codigo_atual
        else:
            self.gerar_codigos(no_atual.no_esquerdo, codigo_atual + "0")
            self.gerar_codigos(no_atual.no_direito, codigo_atual + "1")

    def comprimir(self, texto):
        codigo_comprimido = ""
        for caractere in texto:
            codigo_comprimido += self.codigo[caractere]
        return codigo_comprimido

    def descomprimir(self, codigo_comprimido):
        codigo_atual = ""
        texto_descomprimido = ""
        for bit in codigo_comprimido:
            codigo_atual += bit
            if codigo_atual in self.codigo.values():
                caractere = list(self.codigo.keys())[list(self.codigo.values()).index(codigo_atual)]
                texto_descomprimido += caractere
                codigo_atual = ""
        return texto_descomprimido
    



# Exemplo de uso
texto = "ABRACADABRA"

# Calcular as frequências de cada caractere
frequencias = {}
for caractere in texto:
    if caractere in frequencias:
        frequencias[caractere] += 1
    else:
        frequencias[caractere] = 1

# Construir a árvore de Huffman
noRaiz = No(0,0)
arvore_huffman = Arvore_Huffman(noRaiz)
arvore_huffman.construir_arvore(frequencias)

# Gerar os códigos para cada caractere
arvore_huffman.gerar_codigos(arvore_huffman.no_raiz, "")

# Comprimir o texto usando os códigos gerados
texto_comprimido = arvore_huffman.comprimir(texto)
print("Texto comprimido:", texto_comprimido)

# Descomprimir o texto usando os códigos gerados
#texto_descomprimido =