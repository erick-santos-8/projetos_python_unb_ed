from pythondoido.queue import Queue
from pythondoido.stack import Stack

class pika:
    def operacao(self, s):
        teste = True
        pilha = Stack()
        fila = Queue()
        string = ""
        for i in range(int(len(s)/2)):
            fila.enQueue(s[i])
        for j in range(int(len(s)/2), len(s)):
            pilha.push(s[j])
        while teste:
            string = fila.deQueue()
            string += pilha.pop()
            if string != "()" or string != "{}" or string != "[]":
                teste = False
        if teste:
            return True
        return False
    
piquinha = pika()
print(piquinha.operacao("({[]})"))
