print("CURSO FUNDAMENTOS DE PYTHON")
print("NOMBRE:ARIEL VILLA")
print("FECHA: 30/03/2023")

valor1=int(input("INGRESE VALOR 1= "))
valor2=int(input("INGRESE VALOR 2= "))

operacion=0
print("presionar 1 para sumar")
print("presionar 2 para restar")
print("presionar 3 para multiplicar")

comando=int(input("digite una opcion: "))
if comando==1:
    operacion=valor1+valor2
    print("La sumar es: ",operacion)
elif comando==2:
    operacion=valor1-valor2
    print("La resta es: ",operacion)
elif comando==3:
    operacion=valor1*valor2
    print("La multiplcacion es: ",operacion)
else:
    print("comando no encontrado")





