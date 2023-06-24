class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

    def add_esquerda(self, no_add):
        self.no_esquerdo = no_add

    def add_direito(self, no_add):
        self.no_direito = no_add

class Arvore:
    def __init__(self, no_Raiz):
        self.no_Raiz = no_Raiz
    
    def print_arvore_postorder(self, no):
        if no.no_esquerdo != None:
            self.print_arvore_postorder(no.no_esquerdo)
        if no.no_direito != None:
            self.print_arvore_postorder(no.no_direito)
        print(no.valor)
        
    def print_arvore_preorder(self, no):
        print(no.valor)
        if no.no_esquerdo != None:
            self.print_arvore_preorder(no.no_esquerdo)
        if no.no_direito != None:
            self.print_arvore_preorder(no.no_direito)
            
    def print_arvore_inorder(self, no):
        if no.no_esquerdo != None:
            self.print_arvore_inorder(no.no_esquerdo)
        print(no.valor)
        if no.no_direito != None:
            self.print_arvore_inorder(no.no_direito)
            
    def insereNovoNo(self, noPai, valor):
        if valor < noPai.valor:
            if noPai.no_esquerdo is None:
                novoNo = No(valor)
                noPai.no_esquerdo = novoNo
            else:
                self.insereNovoNo(noPai.no_esquerdo, valor)
        else:
            if noPai.no_direito is None:
                novoNo = No(valor)
                noPai.no_direito = novoNo
            else:
                self.insereNovoNo(noPai.no_direito, valor)

    def conta_nos(self, no):
        contador = 1
        
        if no.no_esquerdo != None:
            contador += self.conta_nos(no.no_esquerdo)
        if no.no_direito != None:
            contador += self.conta_nos(no.no_direito)

        return contador
    
    def altura_arvore(self, no):
        nos_esquerda = self.conta_nos(no.no_esquerdo)
        nos_direita = self.conta_nos(no.no_direito)
        
        if nos_esquerda > nos_direita:
            return nos_esquerda
        return nos_direita
    
    
class Hoffman:
    def __init__(self, no_base_menor, no_base_maior):
        valor_base_no = no_base_maior.valor + 1
        self.no_Base = No(valor_base_no)
        self.no_Base.no_direito(no_base_maior)
        self.no_Base.no_esquerdo(no_base_menor)

        
        self.no_mutavel = No(valor_base_no*2)
        
    def adicionar_no(self, no_Pai):
        
        
    
no1 = No(1)
no2 = No(2)
no3 = No(3)
no4 = No(4)
no5 = No(5)
no6 = No(6)
no7 = No(7)

no1.add_direito(no3)
no1.add_esquerda(no2)
no2.add_direito(no5)
no2.add_esquerda(no4)
no3.add_direito(no7)
no3.add_esquerda(no6)

arvore = Arvore(no1)
arvore.print_arvore_postorder(no1)
print("-----------------------")
arvore.print_arvore_inorder(no1)
print("-----------------------")
arvore.print_arvore_preorder(no1)
print("------------------")
print(arvore.conta_nos(no1))
print("------------------")
print(arvore.altura_arvore(no1))

def frequencia_palavras(texto):
    hash_letras = {}
    for c in texto:
        if c in hash_letras:
            hash_letras[c] += 1
        else:
            hash_letras[c] = 1
    return hash_letras



