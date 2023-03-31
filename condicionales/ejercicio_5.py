print("CURSO FUNDAMENTOS DE PYTHON")
print("NOMBRE:ARIEL VILLA")
print("FECHA: 30/03/2023")

###Ingrese su código
###Ingrese su código
salario=int(input("INGRESE SU SUELDO: "))
impuesto=0
if salario < 10000:
    print("DEBERA PAGAR EL 5% DE IMPUESTO")
    impuesto=0.05
elif salario >=10000 and impuesto < 20000:
    print("DEBERA PAGAR EL 15% DE IMPUESTO")
    impuesto=0.15
elif salario >= 20000 and salario < 35000:
    print("DEBERA PAGAR EL 20% DE IMPUESTO")
    impuesto=0.20
elif salario >= 35000 and salario <= 60000:
    print("DEBERA PAGAR EL 30% DE IMPUESTO")
    impuesto=0.30
elif salario > 60000:
    print("DEBERA PAGAR EL 45% DE IMPUESTO")
    impuesto=0.45
    total= salario*impuesto
else:
    print ("HA PAGADO SUS IMPUESTOS")