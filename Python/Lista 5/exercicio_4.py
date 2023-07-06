from pythonds.graphs import *

class Descobrir:
    def __init__(self, num):
        self.populacao = Graph()
        self.lista_confianca = {}
        for i in range(1, num+1):
            self.populacao.addVertex(i)
            self.lista_confianca[i] = 0
    def descobrir_Juiz(self, lista: list):
        for i in range(len(lista)):
            self.populacao.getVertex(lista[i][0]).addNeighbor(lista[i][1])
            self.lista_confianca[lista[i][1]] += 1
            
        for i in range(1, len(self.lista_confianca)+1):
            if self.lista_confianca[i] == self.populacao.numVertices - 1:
                if len(self.populacao.getVertex(i).getConnections()) == 0:
                    return i
        return -1
    
teste2 = Descobrir(3)
print(teste2.descobrir_Juiz([[1,3],[2,3]]))    

teste1 = Descobrir(2)
print(teste1.descobrir_Juiz([[1,2]]))

teste3 = Descobrir(3)
print(teste3.descobrir_Juiz( [[1,3],[2,3],[3,1]]))
