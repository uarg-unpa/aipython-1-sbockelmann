#punto 13
total=0
promedio=0
for i in range(1,11):
    # precio = float(input(f"Ingrese el precio del producto {i}: "))
     precio = int(1)
     total += precio

promedio = total / 10
promedio = round(promedio, 2)
print(f"El promedio de precios de los 10 productos es: {promedio}")

#punto 14
concatenado='Una ambiciosa'+' '+'Introduccion'+' '+'a Python'+' '+'Parte 1'
print(concatenado)

#punto 15
sociedad= 'aiPython P1'
print(sociedad)
print("la longitud es: ",len(sociedad))
print(sociedad.upper())
print(sociedad.lower())

#punto 16
texto= 'Sometimes it is the people no on imagines anything of who do the things that no one can imagine'
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())

#punto 17
nombre_completo= str(input("Ingrese el nombre completo: "))
for i in range(1,4):
     print(nombre_completo)
