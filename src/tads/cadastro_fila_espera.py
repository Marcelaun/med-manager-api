import itertools as it

class Cadastro_Fila_Espera:
    id_counter = it.count()

    def __init__(self, nome_cliente, horario_de_chegada):
        self.id_chamada = self.id_counter.__next__()
        self.nome_cliente = nome_cliente
        self.horario_chegada = horario_de_chegada


    def __str__(self):
        return f' Id_chamada: {self.id_chamada}\n Nome: {self.nome_cliente}\n Horario_de_chegada: {self.horario_chegada} '




teste_cliente = Cadastro_Fila_Espera('Marcelo', '11:23')
teste_cliente_2 = Cadastro_Fila_Espera('Tiago', '12:34')
print(teste_cliente)
print(teste_cliente_2)