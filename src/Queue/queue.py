from src.Lista.no import Node

class Queue:
    def __init__(self):
        self.inicio = None


    def enqueue(self, valor):
        new_node = Node(valor)

        if self.inicio == None:
            self.inicio = new_node

        else:
            current_first_node = self.inicio
            new_node.proximo = current_first_node
            self.inicio = new_node


    def dequeue(self):
        if self.inicio == None:
            return 'Fila Vazia!'

        else:
            fila = self.inicio
            while fila != None:
                if fila.proximo == None:
                    fila.dados = None


                fila = fila.proximo




    def show_queue(self):
        if self.inicio == None:
            return 'fila vazia!'
        else:
            fila = self.inicio
            while fila != None:
                if fila.dados != None:
                    print(fila.dados)
                fila = fila.proximo




fila_teste = Queue()

fila_teste.enqueue(2)
fila_teste.enqueue(3)
fila_teste.enqueue(4)
fila_teste.enqueue(5)
fila_teste.dequeue()
fila_teste.dequeue()
fila_teste.dequeue()
fila_teste.show_queue()

