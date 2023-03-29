nombre="ARIEL SEBASTIAN"
apellido="VILLA CRESPO"
print(nombre,apellido)

#CONVERTIR DE DATO A TEXTO

numero=int(input("INGRESE EL NUMERO"))
print(type(numero))
cadena=str(numero)
print(type(cadena))

#EJERICIO 1
# EJERCICIOS
#### 1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

 #Si los dos números son iguales
 #Si los dos números son diferentes
 #Si el primero es mayor que el segundo
 #Si el segundo es mayor o igual que el primero

num1=input("Introduce el primer numero")
num2=input("Introduce el segundo numero")
comp1 = num1 == num2
comp1
comp2 = num1 != num2
comp2
comp3 = num1 > num2
comp3
comp4 = num2 >= num1


### 2. Escribir un programa que pregunte el nombre del usuario en la consola y
#  después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola "nombre"!, donde "nombre" es el nombre que el usuario haya introducido.

nombre = input("Introduce tu nombre: ")
print("Hola "+ nombre) 