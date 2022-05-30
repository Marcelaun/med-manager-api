from flask import Flask, request, make_response
from src.Lista.lista import ListaEncadeada

import json

app = Flask(__name__)

lista_medicos = ListaEncadeada()
var_teste = []

@app.route("/")
def homepage():
    return "olá rapaziada"

@app.route("/med-register", methods=['POST'])
def med_register():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json
        print(json)
        if(json):
            # cpf_medico = "98264908921"
            # area_de_atuacao = "Cardiologia"

            lista_medicos.append(json)
            print(var_teste)
            var_teste.append(2)
            # lista_medicos.append(medicstruct1)
            print(var_teste)
            print('passei por aqui')
            return make_response('deu tudo certo', 201)
    else:
        return make_response('request Content not supported!', 500)











@app.route("/med-gather")
def homepage_med():
    dados_medicos = lista_medicos.to_list()
    #json.dumps(dados_medicos.pop())
    json_list = {}
    for value in dados_medicos:
        print(value)
        json_list = json.dumps(dados_medicos.pop())
    print(dados_medicos)
    return json_list


app.run(host='0.0.0.0')
