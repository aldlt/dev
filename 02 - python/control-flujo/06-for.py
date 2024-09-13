buscar = 10
for numero in range(5):
    print(numero)
    #    print(numero, numero * "hola mundo")
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontrre el numero buscado")


for char in "Ultimate Python":
    print(char)
