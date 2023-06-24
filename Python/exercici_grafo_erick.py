class ExercicioGrafo:
    def todosOsCaminhosParaOAlvo(self, graph: list[list[int]]):
        self.grafo = graph
        self.tamanho_grafo = len(graph)
        #todos os possivei caminhos, definitivo
        self.caminhos_possiveis = []
        self.possiblidades(0, [])
        print(self.caminhos_possiveis)

    def possiblidades(self, pos_atual, caminho_percorrido):
        caminho_percorrido.append(pos_atual)
        
        if pos_atual == self.tamanho_grafo - 1:
            self.caminhos_possiveis.append(list(caminho_percorrido))
            #coloquei list na frente do caminho_percorrido para ele fixar o valor, pois se nao colocar, o self.caminhos_possiveis ele aloca a raiz da variavel, assim, ele modifica com o pop()
        
        else:
            for ligacoes_da_posicao in self.grafo[pos_atual]:
                self.possiblidades(ligacoes_da_posicao, caminho_percorrido)
        #o pop serve para excluir o ultimo valor adicionado, pois com a recursao, ele adiciona varios valores, mesmo nao dando em nada
        caminho_percorrido.pop()
                

graph = [[1 , 2], [3], [3],[ ]]
teste = ExercicioGrafo()
teste.todosOsCaminhosParaOAlvo(graph)

graph = [ [ 4 , 3 , 1 ] , [ 3 , 2 , 4 ] , [ 3 ] , [ 4 ] , [ ] ]
teste.todosOsCaminhosParaOAlvo(graph)