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