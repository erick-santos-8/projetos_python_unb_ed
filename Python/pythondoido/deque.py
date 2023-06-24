class Deque:
    def __init__(self):
        self.itens = []
    def append(self, item):
        self.itens.append(item)
    def appendleft(self, item):
        self.itens.insert(0, item)
    def pop(self):
        return self.itens.pop()
    def pop_left(self):
        valor = self.itens[0]
        self.itens.remove(0)
        return valor
    def isEmpty(self):
        return self.itens == []
    def size(self):
        return len(self.itens)
    