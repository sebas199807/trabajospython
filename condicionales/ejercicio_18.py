print("CURSO FUNDAMENTOS DE PYTHON")
print("NOMBRE:ARIEL VILLA")
print("FECHA: 30/03/2023")

palabra = input("Ingrese la palabra a comprobar: ")

if str(palabra) == str(palabra)[::-1] : # Primero calculamos el valor inverso de la palabra original con [::-1] como índice de lista.
    print(f"La palabra ingresada {palabra},si es un Palindromo")
else:
    print(f"La palabra ingresada {palabra},no es Palindromo")
