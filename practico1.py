#TODO: Ejercicio 1 

dia = input("ingrese numero del 1 al 7: ")

match dia:
    case 1:
        print("Su numero corresponde al Lunes")
    case 2:
        print("Su numero corresponde al Martes")
    case 3:
        print("Su numero corresponde al Miercoles")
    case 4:
        print("Su numero corresponde al Jueves")
    case 5:
        print("Su numero corresponde al Viernes")
    case 6:
        print("Su numero corresponde al Sabado")
    case 7:
        print("Su numero corresponde al Domingo")
    case _:
        print("Valor no admitido")

