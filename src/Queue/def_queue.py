class Queue:
    def __init__(self):
        self.fila = []


    def enqueue(self, valor):
        self.fila.append(valor)

    def dequeue(self):
        return self.fila.pop(0)

    def mostrar_fila(self):
        print(f'Fila: {self.fila}')




