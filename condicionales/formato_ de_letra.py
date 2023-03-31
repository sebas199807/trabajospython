#EJERICIO 1
# EJERCICIOS
#### 1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

 #Si los dos números son iguales
 #Si los dos números son diferentes
 #Si el primero es mayor que el segundo
 #Si el segundo es mayor o igual que el primero

num1=int(input("Introduce el primer numero: "))
num2=int (input("Introduce el segundo numero: "))

RESULTADO1 =num1 == num2
RESULTADO2 =num1 != num2
RESULTADO3 =num1 > num2
RESULTADO4 =num2 >= num1

"""
opcion 1
""" 
print("Los numeros"+ str(num1) + "y" +str(num2) + "son iguales:" + str(RESULTADO1))
print("Los numeros" + str(num1) + "y" + str(num2) + "son diferentes " + str(RESULTADO2))
print("El primer numero"+ str(num1) + "es mayor a" + str(num2) + str(RESULTADO3))
print("El segundo numero" + str(num2) + "es mayor o igual a" + str(num1) + str(RESULTADO4))
"""
opcion 2
"""

print(f"LOS NUMEROS {num1} Y {num2} SON IGUALES?:{RESULTADO1}")
print(f"LOS NUMEROS {num1} Y {num2} SON DIFERENTES?:{RESULTADO2}")
print(f"EL PRIMERO {num1} ES MAYOR QUE {num2}?:{RESULTADO3}")
print(f"EL SEGUNDO NUMERO {num2} ES MAYOR O IGUAL QUE {num1}?:{RESULTADO4}")

"""
opcion 3
"""
print("Los numeros",num1,"y",num2,"son iguales:",RESULTADO1)
print("Los numeros",num1,"y",num2,"son diferentes:",RESULTADO2)
print("El primer numero",num1,"es mayor que",num2,"R:",RESULTADO3)
print("El segundo numero",num2,"es mayor o igual que",num1,"R:",RESULTADO4)

"""
opcion 4
"""
print("LOS NUMEROS {} Y {} SON IGUALES?:{}".format(num1, num2, RESULTADO1 ))
print("LOS NUMEROS {} Y {} SON DIFERENTES?:{}".format(num1, num2,RESULTADO2))
print("EL PRIMERO {} ES MAYOR QUE {}?:{}".format(num1,num2,RESULTADO3))
print("EL SEGUNDO NUMERO {} ES MAYOR O IGUAL QUE {}?:{}".format(num1,num2,RESULTADO4))


"""""
OTRO
"""""
### 2. Escribir un programa que pregunte el nombre del usuario en la consola y
#  después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola "nombre"!, donde "nombre" es el nombre que el usuario haya introducido.

nombre = input("Introduce tu nombre: ")
"""
opcion 1
""" 
print("Hola "+ (nombre))

"""
opcion 2
""" 
print(f"Hola {nombre},mucho gusto")
"""
opcion 3
""" 
print("Hola {} mucho gusto".format(nombre))
"""
opcion 4
""" 
print("Hola",nombre,"mucho gusto")
