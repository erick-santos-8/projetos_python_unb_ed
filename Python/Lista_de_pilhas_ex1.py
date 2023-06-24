from pythondoido.queue import Queue

class CircularQueue:
    def __init__(self, tam):
        self.tam = tam
        self.fila = Queue()
    def isFull(self):
        if self.fila.size() < self.tam:
            return False
        return True
    def Front(self):
        if self.fila is not None:
            return self.fila.ValorPos(self.fila.size()-1)
        return -1
    def Rear(self):
        if self.fila is not None:
            return self.fila.ValorPos(0)
        return -1
    def enQueue(self, item):
        if self.isFull() is False:
            self.fila.enQueue(item)
            return True
        return False
    def deQueue(self):
        if self.isFull() is False:
            self.fila.deQueue()
            return True
        return False
    def isEmpty(self):
        return self.fila.isEmpty()

myCircularQueue = CircularQueue(3);
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
print(myCircularQueue.isFull())
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
    
        
        