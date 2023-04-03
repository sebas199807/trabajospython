numero=input("ingrese un numero del 1 al 9: ")

if len(numero) != 1:
    print("ERROR")
elif numero in "0123456789":
    print(f" EL NUMERO {numero} ES CORRECTO")
else:
    print(f"EL NUMERO {numero} ES INCORRECTO")