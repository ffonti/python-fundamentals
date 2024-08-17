#Ereditarietà
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def respira(self):
        print(f"Ciao, mi chiamo {self.nome}")

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def insegna(self):
        print(f"Ciao, mi chiamo {self.nome} e insegno {self.materia}")

p = Persona("Mario", "Rossi")
p.respira()
i = Insegnante("Luca", "Bianchi", "Matematica")
i.respira()
i.insegna()