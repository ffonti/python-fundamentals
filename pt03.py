#Stringhe
stringa_multilinea = """Questa è una stringa
che si estende su più
righe"""

x = "ciao"
y = "mondo"
print(x, y)

nome = "Mario"
print(nome[2])
print(nome[1:3]) # da 1 a 3 (escluso)

frase = "Ciao, come stai?"
print(frase.upper())
print(frase.lower())
print(frase.replace("stai", "va"))
print(frase.split(","))
index_come = frase.find("come")
print(frase[index_come:"come".__len__()+index_come])