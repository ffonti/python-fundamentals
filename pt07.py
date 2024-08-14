#List -> ordinate, modificabili, permettono duplicati, indicizzate
citta = ["Roma", "Milano", "Napoli", "Torino", "Palermo"]
print(citta[citta.__len__()-1])
citta.append("Genova")
print(citta)
citta.insert(1, "Bologna")
print(citta)
citta.remove("Milano")
print(citta)
citta_poppata = citta.pop()
print(citta)
print(citta_poppata)
citta.clear()
print(citta)

#Range -> sequenza di numeri, immutabile, indicizzata
numeri = range(10)
print(numeri)
print(list(numeri)) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
numeri = range(5, 10)
print(list(numeri)) #5, 6, 7, 8, 9
numeri = range(0, 10, 2)
print(list(numeri)) #0, 2, 4, 6, 8
numeri = range(10, 0, -1)
print(list(numeri)) #10, 9, 8, 7, 6, 5, 4, 3, 2, 1
numeri = range(10, 0, -2)
print(list(numeri)) #10, 8, 6, 4, 2


#Tuple -> ordinate, immutabili, permettono duplicati, indicizzate
citta = ("Roma", "Milano", "Napoli", "Torino", "Palermo")
print(citta) #('Roma', 'Milano', 'Napoli', 'Torino', 'Palermo')
print(citta[1]) #Milano
print(citta[-1]) #Palermo
print(citta[1:3]) #('Milano', 'Napoli')
print(citta[-3:-1]) #('Napoli', 'Torino')
print(len(citta)) #5
print(type(citta)) #<class 'tuple'>
print(citta.count("Roma")) #1
print(citta.index("Napoli")) #2
(citta1, citta2, citta3, citta4, citta5) = citta
print(citta1) #Roma

#Set -> non ordinate, modificabili, non permettono duplicati, non indicizzate
citta = {"Roma", "Milano", "Napoli", "Torino", "Palermo", "Palermo"}
print(citta) #{'Napoli', 'Roma', 'Milano', 'Torino', 'Palermo'}
citta.add("Genova")
altre_citta = {"Firenze", "Bologna"}
citta.update(altre_citta)
print(citta) #{'Napoli', 'Roma', 'Milano', 'Torino', 'Palermo', 'Genova', 'Firenze', 'Bologna'}
citta.remove("Milano") #genera errore se l'elemento non esiste
print(citta) #{'Napoli', 'Roma', 'Torino', 'Palermo', 'Genova', 'Firenze', 'Bologna'}
citta.discard("Milano") #non genera errore se l'elemento non esiste
print(citta) #{'Napoli', 'Roma', 'Torino', 'Palermo', 'Genova', 'Firenze', 'Bologna'}
citta.clear()
print(citta) #set()

#Dictionary -> ordinate, modificabili, non permettono duplicati, indicizzate
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}
print(persona) #{'nome': 'Luca', 'cognome': 'Rossi', 'eta': 25}
print(persona["nome"]) #Luca
print(persona.get("cognome")) #Rossi
print(persona.get("altezza")) #None
persona["altezza"] = 180
print(persona) #{'nome': 'Luca', 'cognome': 'Rossi', 'eta': 25, 'altezza': 180}
persona.pop("eta")
print(persona) #{'# nome': 'Luca', 'cognome': 'Rossi', 'altezza': 180}
persona.update({"scuola": "ITIS"})
print(persona) #{'nome': 'Luca', 'cognome': 'Rossi', 'altezza': 180, 'scuola': 'ITIS'}
print(persona.keys()) #dict_keys(['nome', 'cognome', 'altezza'])
print(persona.values()) #dict_values(['Luca', 'Rossi', 180])
print(persona.items()) #dict_items([('nome', 'Luca'), ('cognome', 'Rossi'), ('altezza', 180])
if "nome" in persona:
    print("Si")
persona.clear()
print(persona) #{}
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
    "indirizzo": {
        "via": "Via Roma",
        "citta": "Roma",
        "cap": "00100"
    }
}
print(persona["indirizzo"]["citta"]) #Roma