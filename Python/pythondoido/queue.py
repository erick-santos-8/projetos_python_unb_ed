class Queue:
    def __init__(self):
        self.lista = []
    def isEmpty(self):
        return self.itens == []
    def enQueue(self, item):
        self.lista.insert(0, item)
    def deQueue(self):
        return self.lista.pop(0)
    def size(self):
        return len(self.lista)
    def peek(self):
        return self.lista[0]