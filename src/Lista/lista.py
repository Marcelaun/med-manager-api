from src.Lista.no import Node
from flask import jsonify

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




    def pesquisa_medicos_por_area_atuacao(self, dados):
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




    def remover_cadastro(self, informacoes):
        current_node = self.inicio

        if current_node != None:
            if current_node.dados == informacoes:
                self.inicio = current_node.proximo
                current_node = None
                return

            while current_node != None:
                if current_node.dados == informacoes:
                    break
                prev = current_node
                current_node = current_node.proximo

        if current_node == None:
            return ("lisa vazia")

        prev.proximo = current_node.proximo
        current_node = None





patient = {
    "nome": "Marcelo Almeida Barbosa",
    "data_nasc": "2022-08-19",
    "cpf": "14946804676",
    "rg": "21381230",
    "tel": "3998231101",
    "email": "cellort567@gmail.com",
    "endereco": {
        "rua": "trazibulo jason",
        "bairro": "Sao Pedro",
        "cidade": "Almenara",
        "estado": "MG",
        "numero": "1143",
        "cep": "39900000"
    },
    "cartao_sus": "338847632"
}

patient2 = {
    "nome": "Marcelo Almeida Barbosa",
    "data_nasc": "2022-08-19",
    "cpf": "00564801640",
    "rg": "21381230",
    "tel": "3998231101",
    "email": "cellort567@gmail.com",
    "endereco": {
        "rua": "trazibulo jason",
        "bairro": "Sao Pedro",
        "cidade": "Almenara",
        "estado": "MG",
        "numero": "1143",
        "cep": "39900000"
    },
    "cartao_sus": "338847632"
}

patient3 = {
    "nome": "Marcelo Almeida Barbosa",
    "data_nasc": "2022-08-19",
    "cpf": "88999887626",
    "rg": "21381230",
    "tel": "3998231101",
    "email": "cellort567@gmail.com",
    "endereco": {
        "rua": "trazibulo jason",
        "bairro": "Sao Pedro",
        "cidade": "Almenara",
        "estado": "MG",
        "numero": "1143",
        "cep": "39900000"
    },
    "cartao_sus": "338847632"
}


cpf = "00564801640"

lista_medicos = ListaEncadeada()
# dados medicos
medic = {
    "nome": "Marcelo Almeida Barbosa",
    "data_nasc": "2022-08-19",
    "cpf": "88999887626",
    "rg": "21381230",
    "tel": "3998231101",
    "email": "cellort567@gmail.com",
    "endereco": {
        "rua": "trazibulo jason",
        "bairro": "Sao Pedro",
        "cidade": "Almenara",
        "estado": "MG",
        "numero": "1143",
        "cep": "39900000"
    },
    "area-of-action": "Cardiologia",
    "specialization": "Tomografia computadorizada",
    "crm": {
        "number": "056024",
        "uf": "SP"
    },
    "horarios": {
        "days": {
            "segunda": {
                "horario_atendimento": "13h as 19h",
                "periodo_dia": "tarde"
            },
            "terça": {
                "horario_atendimento": "13h as 19h",
                "periodo_dia": "tarde"
            }
        }
    }

}

medic2 = {
    "nome": "Marcelo Almeida Barbosa",
    "data_nasc": "2022-08-19",
    "cpf": "7632370987",
    "rg": "21381230",
    "tel": "3998231101",
    "email": "cellort567@gmail.com",
    "endereco": {
        "rua": "trazibulo jason",
        "bairro": "Sao Pedro",
        "cidade": "Almenara",
        "estado": "MG",
        "numero": "1143",
        "cep": "39900000"
    },
    "area-of-action": "Cardiologia",
    "specialization": "Tomografia computadorizada",
    "crm": {
        "number": "056024",
        "uf": "SP"
    },
    "horarios": {
        "days": {
            "segunda": {
                "horario_atendimento": "13h as 19h"
            },
            "terça": {
                "horario_atendimento": "13h as 19h"
            }
        }
    }

}

medic3 = {
    "nome": "Marcelo Almeida Barbosa",
    "data_nasc": "2022-08-19",
    "cpf": "98264908921",
    "rg": "21381230",
    "tel": "3998231101",
    "email": "cellort567@gmail.com",
    "endereco": {
        "rua": "trazibulo jason",
        "bairro": "Sao Pedro",
        "cidade": "Almenara",
        "estado": "MG",
        "numero": "1143",
        "cep": "39900000"
    },
    "area-of-action": "Cardiologia",
    "specialization": "Tomografia computadorizada",
    "crm": {
        "number": "056024",
        "uf": "SP"
    },
    "horarios": {
        "days": {
            "segunda": {
                "horario_atendimento": "13h as 19h"
            },
            "terça": {
                "horario_atendimento": "13h as 19h"
            }
        }
    }

}

# cpf_medico = "98264908921"
# area_de_atuacao = "Cardiologia"

lista_medicos.append(medic)
lista_medicos.append(medic2)
lista_medicos.append(medic3)

dados_medicos = lista_medicos.display()
print(dados_medicos)

