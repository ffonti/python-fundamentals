#Scope
x = 300 #Scope globale

def fun():
    y = 200 #Scope locale
    print("Stampo x dentro la funzione")
    print(x)
    print("Stampo y dentro la funzione")
    print(y)

fun()
print("Stampo x fuori dalla funzione")
print(x)
print("Stampo y fuori dalla funzione")
#print(y) Errore: y non è definito

num = 100

def fun2():
    num = 200
    print("Stampo num dentro la funzione")
    print(num)

fun2()

def fun3():
    global num
    num = 300
    print("Stampo num dentro la funzione")
    print(num)

fun3()