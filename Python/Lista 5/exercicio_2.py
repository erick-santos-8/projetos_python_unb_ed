from pythonds.basic import *
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
    def __init__(self, raiz):
        self.raiz = raiz
    
    def print_Inorder(self, noPai):
        if noPai.no_esq != None:
            self.print_Inorder(noPai.no_esq)
        print(noPai.valor)
        if noPai.no_dir != None:
            self.print_Inorder(noPai.no_dir)
    
    def verificar_semelhanca(self, noPai: No):
        deque_funcao = Deque()
        if noPai.no_esq is not None:
            deque_funcao.addFront(self.armazenar_valor_deque(noPai.no_esq, deque_funcao))
        
        if noPai.no_dir is not None:
            deque_funcao.addRear(self.armazenar_valor_deque(noPai.no_dir, deque_funcao))
            
        while deque_funcao.size()>1:
            julgador_igualdade = True
            var_final = deque_funcao.removeRear()
            var_frontal = deque_funcao.removeFront()
            if var_frontal == None:
                var_frontal = deque_funcao.removeFront()
            if var_final == None:
                var_final = deque_funcao.removeRear()
            if var_final != var_frontal:
                julgador_igualdade = False
        return julgador_igualdade
    
    def armazenar_valor_deque(self, noPai, deque_funcao):
        if noPai.no_esq is not None:
            self.armazenar_valor_deque(noPai.no_esq, deque_funcao)
        deque_funcao.addFront(noPai.valor)
        if noPai.no_dir is not None:
            self.armazenar_valor_deque(noPai.no_dir, deque_funcao)
       

no1 = No(1)
no1.add_Dir(2)
no1.no_dir.add_Dir(3)
no1.no_dir.add_Esq(4)

no1.add_Esq(2)
no1.no_esq.add_Dir(4)
no1.no_esq.add_Esq(3)

arvore = Arvore(no1)
arvore.print_Inorder(no1)
print(arvore.verificar_semelhanca(no1))