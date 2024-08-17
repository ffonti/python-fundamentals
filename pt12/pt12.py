#Moduli
import miomodulo as mm #importa il modulo miomodulo con il nome mm (alias)
import platform
import math
from miomodulo import persona #importa solo la variabile persona dal modulo miomodulo
from pt02 import cognome

mm.saluta("Fabrizio")

x = mm.persona["nome"]
print(x)

print(platform.system())
print(math.floor(2.9))
print(dir(math)) #elenco delle funzioni del modulo math
print(help(math.floor)) #help per la funzione floor del modulo

p = persona
print(p["cognome"])