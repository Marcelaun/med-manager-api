from flask import Flask, jsonify
from src.Lista.lista import ListaEncadeada
from src.tads.medico import Medico
from src.tads.paciente import Paciente
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    return "olá rapaziada"


@app.route("/med-gather")
def homepage_med():

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



    dados_medicos = lista_medicos.to_list()
    json_list = json.dumps(dados_medicos.pop())
    print(json_list)
    return json_list


app.run(host='0.0.0.0')
