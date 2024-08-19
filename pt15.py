#JSON
import json
from textwrap import indent

from pt03 import index_come

x = '{ "nome": "Fabrizio", "cognome": "Fontana", "eta":"21"}'
y = json.loads(x)
print(y) # {'nome': 'Fabrizio', 'cognome': 'Fontana', 'eta': '21'}
print(y["nome"]) # Fabrizio
print(type(y)) # <class 'dict'>

n = {
    "nome": "Fabrizio",
    "cognome": "Fontana",
    "eta":"21"
}
# ho indentato con 4 spazi, ho messo un punto e uno spazio tra le chiavi
# e i valori e ho messo un uguale tra le chiavi e i valori
m = json.dumps(n, indent=4, separators=(". ", "= "), sort_keys=True)
print(m) # {"nome": "Fabrizio", "cognome": "Fontana", "eta": "21"}
print(type(m)) # <class 'str'>
