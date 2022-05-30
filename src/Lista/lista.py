from src.Lista.no import Node
from flask import jsonify
from src.tads.medico import Medico

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def append(self, dados):
        new_node = Node(dados)

        if self.inicio == None:
            self.inicio = new_node
            return

        current_node = self.inicio

        while current_node.proximo:
            current_node = current_node.proximo

        current_node.proximo = new_node
        return

# retorna o tamanho da lista
    def length(self):
        if self.inicio == None:
            return 0
        current_node = self.inicio
        total = 0

        while current_node:
            total += 1
            current_node = current_node.proximo
        return total



# transforma a lista em um array
    def to_list(self):
        node_data = []
        current_node = self.inicio

        while current_node:
            node_data.append(current_node.dados)
            current_node = current_node.proximo

        return node_data

    #display dados na lista

    def display(self):
        contents = self.inicio
        content_array = []

        if contents is None:
            print("lista vazia")

        while contents:
            content_array.append(contents.dados)
            contents = contents.proximo

        print('--------')
        return content_array



    def pesquisa_paciente(self, dados):
        contents = self.inicio
        if contents is None:
            print("lista vazia!")

        while contents:
            dados_atuais = contents.dados
            if dados in dados_atuais.values():
                print("dados atuais", dados_atuais)
                print(f"value: {dados}")
                return dados_atuais

            contents = contents.proximo

    def pesquisa_medico(self, dados):
        contents = self.inicio
        if contents is None:
            print("lista vazia!")

        while contents:
            dados_atuais = contents.dados
            if dados in dados_atuais.values():
                print("dados atuais", dados_atuais)
                print(f"value: {dados}")
                return dados_atuais

            contents = contents.proximo




    def pesquisa_medicos_por_area_atuacao(self, area_value):
        contents = self.inicio
        content_array = []
        if contents is None:
            print("lista vazia!")

        while contents:
            dados_atuais = contents.dados
            if dados in dados_atuais.values():
                print("dados atuais", dados_atuais)
                print(f"value: {dados}")
                content_array.append(dados_atuais)

            contents = contents.proximo

        return content_array




    def remover_cadastro(self, cpf):

        if self.inicio is None:
            return

        left_node = None
        curr_node = self.inicio
        cpf_atual = curr_node.dados.cpf

        if cpf_atual == cpf:
            self.inicio = curr_node.proximo

        while True:
            left_node = curr_node
            curr_node = curr_node.proximo

            if curr_node is None:
                break

            if curr_node.dados.cpf == cpf:
                left_node.proximo = curr_node.proximo





