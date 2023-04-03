print("CURSO FUNDAMENTOS DE PYTHON")
print("NOMBRE:ARIEL VILLA")
print("FECHA: 30/03/2023")

#PROBLEMA 1
#Crear un programa que permita decidir a una persona cruzar la calle o no según:
# Si semáforo esta en verde cruzar la calle
#Si semáforo esta en rojo o amarillo no cruzar

#La persona debe poder ingresar el estado del semáforo por teclado
#
semaforo=input("INGRESE EL COLOR DEL SEMAFORO: ")
if semaforo=="verde":
    print("USTED PUEDE CRUZAR")
elif  semaforo =="amarillo":
    print("USTED TIENE QUE ESPERAR")
elif semaforo =="rojo":
    print ("NO CRUZAR")
else:
    print("NO ES EL COLOR CORRECTO")