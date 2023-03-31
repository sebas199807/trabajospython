letra=input("ingrese una letra: ")
if len (letra) != 1:
    print("no se puede procesar el dato. debe ingresar una sola letra")
elif letra in "aeiuoAEIOU":
    print ("es vocal")
else:
    print("es parte del abecedario")