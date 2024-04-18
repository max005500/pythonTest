#TODO: Ejercicio 3

pass1 = input("Ingrese contraseña: ")
pass2 = input("confirme su contraseña: ")

while pass1 != pass2:
    print("vuelva a intentarlo")
    pass1 = input("Ingrese contraseña: ")
    pass2 = input("confirme su contraseña: ")
        
print("Contraseña correcta")
