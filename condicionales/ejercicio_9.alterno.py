calificacion=float(input("INGRESE SU CALIFICACION: "))

if calificacion >= 0.00 and calificacion < 4.00:
    print("SU NOTA ES DEFICIENTE")
elif calificacion >= 4.00 and calificacion < 7.00:
    print("SU NOTA ES REGULAR")
elif calificacion >= 7.00 and calificacion < 8.50:
    print("SU NOTA ES BUENO")
elif calificacion >= 8.50 and calificacion < 9.50:
    print("SU NOTA ES MUY BUENA")
elif calificacion >= 9.50 and calificacion <= 10.00:
    print("SU NOTA ES EXCELENTE")
else:
    print("LA NOTA ES INCORRECTA")

