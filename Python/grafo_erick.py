class Vertice:
    def __init__(self, id):
        self.id = id
        
class Arestas:
    def __init__(self):
        self.hash_Id = {}
    
    def add_Arestas(self, vertice_origem, vertice_final, peso):
        hash_reuso = {}
        try:
            hash_reuso = self.hash_Id[vertice_origem.id]
            hash_reuso[vertice_final.id] = peso
            self.hash_Id[vertice_origem.id] = hash_reuso
        except:
            self.hash_Id[vertice_origem.id] = {vertice_final.id: peso}
        
        print(self.hash_Id)
        
v1 = Vertice(1)
v2 = Vertice(2)
v3 = Vertice(3)
v4 = Vertice(4)
arestas = Arestas()
arestas.add_Arestas(v1, v2, 2)
arestas.add_Arestas(v1, v3, 6)
arestas.add_Arestas(v4, v2, 4)