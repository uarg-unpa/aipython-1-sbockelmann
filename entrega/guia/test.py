print("Nombre\tEdad\tPais\tCiudad")
print("Alexa\t250\tUSA\tCapeCod")

edad_usuario1=int (input("Ingrese la edad del cliente: "))
if edad_usuario1 < 4:
    print("puede pasar gratis")
elif edad_usuario1 > 4 and edad_usuario1 < 8:
    print("Debe pagar $5")
else:
    print("Debe pagar $10")