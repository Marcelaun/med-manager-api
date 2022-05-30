from flask import jsonify
from src.Lista.lista import ListaEncadeada

class Paciente:
    def __init__(self, nome, cpf ,rg, data_nascimento, telefone, email, endereco, cartao_sus):
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


    def __str__(self):
        return f'nome: {self.nome}\n cpf: {self.cpf}\n rg: {self.rg}\n email: {self.email}\n telefone: {self.telefone}\n endereço: {self.endereco}\n cartao_sus: {self.cartao_sus}\n  -------------------------------------------------------- '