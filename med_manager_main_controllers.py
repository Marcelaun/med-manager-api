from src.Lista.lista import ListaEncadeada
from src.Queue.def_queue import Queue
import PySimpleGUI as sg
import datetime as dt
fila_clientes = Queue()
lista_medicos = ListaEncadeada()
lista_pacientes = ListaEncadeada()

from src.tads.medico import Medico
from src.tads.paciente import Paciente
from src.tads.cadastro_fila_espera import Cadastro_Fila_Espera

def second_window():

    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],
              [sg.OK()]]

    window = sg.Window('Second Form', layout)
    event, values = window.read()
    window.close()

def pacient_register_window():
    layout = [[sg.Text('Insira os dados do paciente por aqui.')],
              [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
              [sg.Text('CPF:', size=(15, 1)), sg.InputText()],
              [sg.Text('RG:', size=(15, 1)), sg.InputText()],
              [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText()],
              [sg.Text('Telefone:', size=(15, 1)), sg.InputText()],
              [sg.Text('Email:', size=(15, 1)), sg.InputText()],
              [sg.Text('Endereço:', size=(15, 1)), sg.InputText()],
              [sg.Text('Cartão do SUS:', size=(15, 1)), sg.InputText()],
              [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]]

    window = sg.Window('Cadastro de Pacientes', layout)
    event, values = window.read()
    novo_paciente = Paciente(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])
    print(novo_paciente)
    lista_pacientes.append(novo_paciente)

    window.close()


def medic_register_window():
    layout = [[sg.Text('Insira os dados do médico por aqui.')],
              [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
              [sg.Text('CPF:', size=(15, 1)), sg.InputText()],
              [sg.Text('RG:', size=(15, 1)), sg.InputText()],
              [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText()],
              [sg.Text('Telefone:', size=(15, 1)), sg.InputText()],
              [sg.Text('Email:', size=(15, 1)), sg.InputText()],
              [sg.Text('Endereço:', size=(15, 1)), sg.InputText()],
              [sg.Text('Área/Atuação:', size=(15, 1)), sg.InputText()],
              [sg.Text('Especialização:', size=(15, 1)), sg.InputText()],
              [sg.Text('Horário:', size=(15, 1)), sg.InputText()],
              [sg.Text('CRM:', size=(15, 1)), sg.InputText()],
              [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]]

    window = sg.Window('Cadastro de Médicos', layout)
    event, values = window.read()
    novo_medico = Medico(
        values[0], values[1], values[2], values[3], values[4], values[5],
        values[6], values[7], values[8], values[9], values[10])
    print(novo_medico)
    lista_medicos.append(novo_medico)
    window.close()

def pacient_listing_window():
    lista_pacientes_atual = lista_pacientes.to_list()
    for paciente in lista_pacientes_atual:
        print(paciente)

def medic_listing_window():
    lista_medicos_atual = lista_medicos.to_list()
    print('chegou aq')
    for medico in lista_medicos_atual:
        print(medico)


def remove_pacient_window():
    layout = [[sg.Text('Insira o CPF do paciente.')],
              [sg.Text('CPF:', size=(15, 1)), sg.InputText()],
              [sg.Text('-------------------------------------------------------------------------'
                       '------------------------------------------------------------------')],
              [sg.Text('Chamar cliente para atendimento.')],
              [sg.Button('Deletar'), sg.Cancel('Cancelar')]

              ]

    window = sg.Window('Remover Cadastro de Pacientes', layout)
    event, values = window.read()


def remove_medic_window():
    layout = [[sg.Text('Insira o CPF do médico.')],
              [sg.Text('CPF:', size=(15, 1)), sg.InputText()],
              [sg.Text('-------------------------------------------------------------------------'
                       '------------------------------------------------------------------')],

              [sg.Button('Deletar'), sg.Cancel('Cancelar')]

              ]

    window = sg.Window('Remover Cadastro de Medicos', layout)
    event, values = window.read()

    if event == 'Deletar':
        pop_up_value = sg.popup_yes_no('Tem certeza que deseja deletar esse registro?')
        if pop_up_value == 'Yes':
            print('entrou no yes')
            lista_medicos.remover_cadastro(values[0])
            lista_medicos.display()
        elif pop_up_value == 'No':
            print('entrou no No')


    window.close()


def day_queue_attendance():

    layout = [[sg.Text('Insira os dados do cliente por aqui.')],
              [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
              [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')],
              [sg.Text('-------------------------------------------------------------------------'
                       '------------------------------------------------------------------')],
              [sg.Text('Chamar cliente para atendimento.')],
              [sg.Button('Chamar')]


              ]

    window = sg.Window('Fila de atendimento', layout)
    event, values = window.read()
    if event == 'Chamar':
        fila_clientes.dequeue()
        fila_clientes.mostrar_fila()
    else:
        data_atual = dt.datetime.now()
        horario_atual = f'{data_atual.hour}:{data_atual.minute}:{data_atual.second}'
        novo_cliente = Cadastro_Fila_Espera(values[0], horario_atual)
        fila_clientes.enqueue(novo_cliente.__str__())
        fila_clientes.mostrar_fila()




    window.close()
def test_menus():

    sg.theme('LightGreen')
    sg.set_options(element_padding=(0, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&Salvar', ['&Salvar Dados       Ctrl-S', '&Sair do programa']],
                ['&Cadastro', ['---', '&Cadastro de Médicos', '&Cadastro de Pacientes']],
                ['&Listagem', ['---', '&Listar Médicos', '&Listar Pacientes']],
                ['&Remover Cadastros', ['---', '&Remover Médico', '&Remover Paciente']],
                ['&Fila de Espera', ['&Fila de atendimento do dia']],
                ['&Ajuda', '&Sobre...'], ]

    right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Propriedades']]

    # ------ GUI Defintion ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Text('Bem vindo!')],
        [sg.Output(size=(100, 30))],
    ]

    window = sg.Window("Med-Manager",
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       right_click_menu=right_click_menu)

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Sair do programa'):
            break
        print(event, values)
        # ------ Process menu choices ------ #
        if event == 'Sobre...':
            window.disappear()
            sg.popup('Sobre esse programa', 'Versão 1.0',
                     'Versão PySimpleGui', sg.version,  grab_anywhere=True)
            window.reappear()
        elif event == 'Propriedades':
            second_window()

        elif event == 'Cadastro de Pacientes':
            pacient_register_window()

        elif event == 'Cadastro de Médicos':
            medic_register_window()

        elif event == 'Listar Médicos':
            medic_listing_window()

        elif event == 'Listar Pacientes':
            pacient_listing_window()

        elif event == 'Fila de atendimento do dia':
            day_queue_attendance()

        elif event == 'Remover Médico':
            remove_medic_window()

        elif event == 'Remover Paciente':
            remove_pacient_window()



    window.close()


test_menus()