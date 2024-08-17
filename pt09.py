#OOP
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} {self.cognome} e ho {self.eta} anni")

persona1 = Persona("Mario", "Rossi", 30)
persona2 = Persona("Luca", "Bianchi", 25)

persona1.saluta()
persona2.saluta()

persona2.nome = "Maria"
persona2.saluta()

del persona2 #Elimina l'oggetto persona2