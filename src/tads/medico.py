class Medico:
    def __init__(self, nome, cpf, rg, telefone, email, endereco, area_atuacao, especializacao, numero_reg, horario):

        if nome == '' or cpf == '' or area_atuacao == '' or especializacao == '' or numero_reg == '' or horario == '':
            print('Dados obrigatorios do médico faltando!!')
            return
        else:
            self.nome = nome
            self.rg = rg
            self.cpf = cpf
            self.telefone = telefone
            self.email = email
            self.endereco = endereco
            self.area_atuacao = area_atuacao
            self.especializacao = especializacao
            self.horario = horario
            self.num_registro = numero_reg

