from localStoragePy import localStoragePy
from json import dumps


med_list_localStorage = localStoragePy('med-list-localSotrage', 'json')
pacient_list_Storage = localStoragePy('pacient-list-localStorage', 'json')


test_json = {"nome": "marcelo"}
test_json_2 = {"nome": "tiago"}

def postMedInStorage(med_data):
    med_list_localStorage.setItem('valor_teste', med_data)
    print(med_list_localStorage.getItem('valor_teste'))
    valor_atual = med_list_localStorage.getItem('valor_teste')
    novos_valores = [valor_atual, med_data]
    med_list_localStorage.setItem('valor_teste', dumps(novos_valores))
    print(med_list_localStorage.getItem('valor_teste'))


postMedInStorage(test_json)