class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_completo = []
        self.no_completo.append(valor)
        
    def adicionar_filhos(self, no_filho):
        self.no_completo.append(no_filho)
        print(self.no_completo)
    
class Arvore:
    def __init__(self, no_raiz):
        self.no_raiz = no_raiz
        self.no_completo = []
        self.no_completo.append(self.no_raiz)
    
    def print_arvore(self):
        print(self.no_completo)
        
