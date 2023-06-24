class Simple_string:
    def __init__(self, string):
        self.string = string.strip()
        self.operacao_ant = None
        self.numeros_adicionados = None
    
    def Anexar(self, item):
        self.string.append(item)
        self.operacao_ant = f"1 {item}"
    
    def Delete(self, num):
        i = 0
        self.operacao_ant = f"2 {num}"
        while i < num:
            self.numeros_adicionados.append(self.string[len(self.string)-1])
            self.string.pop()
            i += 1
    def Imprimir(self, num):
        print(self.string[num])
    def Undo(self):
        list_op_ant = self.operacao_ant.strip()
        ref = ["1": "Delete", "2": "Anexar"]
        if list_op_ant[0] == ref[1]:
            self.Delete(1)
        else:
            for i in range(len(self.numeros_adicionados), 0):
                self.Anexar(self.numeros_adicionados[i])
class 
    