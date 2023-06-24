class Queue:
    def __init__(self):
        self.lista = []
    def isEmpty(self):
        return self.itens == []
    def enQueue(self, item):
        self.lista.insert(0, item)
    def deQueue(self):
        return self.lista.pop()
    def size(self):
        return len(self.lista)
    def ValorPos(self, pos):
        if self.size() > pos:
            return self.lista[pos]
        return -1

def separar_e_retornar(string):
    ref_queue = Queue()
    string = string.split()
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i][j] is "*":
                ref_queue.d
                
            