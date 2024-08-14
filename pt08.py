#Funzioni
def saluta(nome):
    print("Ciao,", nome + "!")
nome = input("Come ti chiami? ")
saluta(nome)

def somma(a, b):
    return a + b
a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un altro numero: "))
print("La somma è", somma(a, b))

def stampa_ingredienti(*ingredienti):
    print("Ingredienti:")
    for ingrediente in ingredienti:
        print("-", ingrediente.capitalize())
stampa_ingredienti("farina", "uova", "zucchero")

def fai_la_pasta(ricetta, sugo):
    print(ricetta)
    if sugo:
        print("Anche il sugo")
fai_la_pasta(sugo = False, ricetta = "Pasta al pomodoro")

def saluta(nome = "Mondo"):
    print("Ciao,", nome + "!")
saluta()
saluta("Alice")