from flask import jsonify
from src.Lista.lista import ListaEncadeada

class Paciente:
    def __init__(self, nome, data_nascimento, cpf, rg, telefone, email, endereco, cartao_sus):
        if nome == '' or cpf == '' or cartao_sus == '':
            print('Dados obrigatorios do paciente faltando!!')
            return
        else:
            self.nome = nome
            self.rg = rg
            self.cpf = cpf
            self.data_nasc = data_nascimento
            self.telefone = telefone
            self.email = email
            self.endereco = endereco
            self.cartao_sus = cartao_sus

