class Medico:
    def __init__(self, nome, cpf, rg, data_nasc, telefone, email, endereco, area_atuacao, especializacao, horario, numero_reg):

        if nome == '' or cpf == '' or area_atuacao == '' or especializacao == '' or numero_reg == '' or horario == '':
            print('Dados obrigatorios do médico faltando!!')
            return
        else:
            self.nome = nome
            self.rg = rg
            self.cpf = cpf
            self.telefone = telefone
            self.data_nascimento = data_nasc
            self.email = email
            self.endereco = endereco
            self.area_atuacao = area_atuacao
            self.especializacao = especializacao
            self.horario = horario
            self.num_registro = numero_reg


    def __str__(self):
        return f'nome: {self.nome}\n cpf: {self.cpf}\n rg: {self.rg}\n email: {self.email}\n data_nascimento: {self.data_nascimento}\n telefone: {self.telefone}\n endereço: {self.endereco}\n horario: {self.horario}\n especializacao: {self.especializacao}\n area_atuacao: {self.area_atuacao}\n num_registro: {self.num_registro}\n  ------------------------------------------------ '





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