from pythonds.graphs import *

# populacao = Graph()
# pessoa1 = populacao.addVertex(1)
# pessoa1.addNeighbor(3)
# pessoa2 = populacao.addVertex(2)
# pessoa2.addNeighbor(3)
# pessoa3 = populacao.addVertex(3)

class Descobrir:
    def __init__(self, num):
        self.populacao = Graph()
        self.pessoas = []
        self.lista_confianca = {}
        for i in range(1, num+1):
            self.pessoas.append(self.populacao.addVertex(i))
            self.lista_confianca[i] = 0
    def descobrir_Juiz(self, lista: list):
        for i in range(len(lista)):
            self.pessoas[lista[i][0]-1].addNeighbor(lista[i][1])
            self.lista_confianca[lista[i][1]] += 1
        
        for i in range(1, len(self.lista_confianca)+1):
            if self.lista_confianca[i] == self.populacao.numVertices - 1:
                if len(self.pessoas[i-1].getConnections()) == 0:
                    return i
        return -1
    
teste2 = Descobrir(3)
print(teste2.descobrir_Juiz([[1,3],[2,3]]))    

teste1 = Descobrir(2)
print(teste1.descobrir_Juiz([[1,2]]))

teste3 = Descobrir(3)
print(teste3.descobrir_Juiz( [[1,3],[2,3],[3,1]]))