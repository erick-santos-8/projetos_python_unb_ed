class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esq = None
        self.no_dir = None
        
    def add_Esq(self, valor_No):
        no_esquerdo = No(valor_No)
        self.no_esq = no_esquerdo
    
    def add_Dir(self, valor_No):
        no_direito = No(valor_No)
        self.no_dir = no_direito    
        
class Arvore:
    def __init__(self, valor):
        self.valor_inicial = valor
        
    def balanceamento(self, no_Pai):
        if no_Pai.no_esq != None:
            tam_esq = self.tamanho_no(no_Pai.no_esq)
        if no_Pai.no_dir != None:
            tam_dir = self.tamanho_no(no_Pai.no_dir)
        if abs(tam_esq - tam_dir) > 1:
            print("Não balanceada!")
        else:
            print("Balanceada")
            
    def tamanho_no(self, noPai):
        contador_esq = 1
        contador_dir = 1
        if noPai.no_esq != None:
            contador_esq += self.tamanho_no(noPai.no_esq)
        if noPai.no_dir != None:
            contador_dir += self.tamanho_no(noPai.no_dir)
        if contador_esq > contador_dir:
            return contador_esq
        return contador_dir
    
no3 = No(3)
no3.add_Dir(20)
no3.no_dir.add_Dir(7)
no3.no_dir.add_Esq(15)
no3.add_Esq(9)
arvore1 = Arvore(no3)
arvore1.balanceamento(no3)

no1 = No(1)
no1.add_Dir(2)
no1.add_Esq(2)
no1.no_esq.add_Esq(3)
no1.no_esq.add_Dir(3)
no1.no_esq.no_esq.add_Esq(4)
no1.no_esq.no_dir.add_Dir(4)
arvore2 = Arvore(no1)
arvore2.balanceamento(no1)
