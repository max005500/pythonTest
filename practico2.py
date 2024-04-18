#TODO: Ejercicio 2:

try:
    edad = int(input("Ingrese su edad: "))
    exp = int(input("Tiene experiencia programando en pytho (1=si o 0=no): "))

    if edad >= 60 or edad <= 18 or exp == 0:
        print("No Elegible")
    elif exp != 1:
        print("ingrese su experiencia con un numero entre 0 y 1")
    else:
        print("Elegible")
except:
    print("Ingrese solo valores numericos")


