print("CURSO FUNDAMENTOS DE PYTHON")
print("NOMBRE:ARIEL VILLA")
print("FECHA: 30/03/2023")

año=int(input("ingresa año\n"))
if(año % 4 == 0 and año % 100 != 0 or año % 400 == 0):
 print("El año "+str(año)+" Si es bisiesto ")
else:
 print("El año "+str(año)+" No es bisiesto ")