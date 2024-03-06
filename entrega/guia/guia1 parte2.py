#punto 13
total=0
promedio=0
for i in range(1,11):
    #precio = float(input(f"Ingrese el precio del producto {i}: "))
    precio = 1 #prueba
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
print(nombre_completo *3)

#punto 18
print("            *")
print("          *   *")
print("         *     *")
print("        *       *")
print("       *         *")
print("      *           *")
print("     *             *")
print("    ******        ****")
print("         *       *")
print("         *       *")
print("         *       *")
print("         *       *")
print("         *********")

#punto 19
print("      *","\n","   *   *","\n","  *     *","\n"," *       *","\n","***     ***","\n","   *   *","\n","   *   *","\n","   *****")

print("punto 20")
#punto 20
print("      *","\n","   *   *","\n","  *     *","\n"," *       *","\n","***     ***","\n","   *   *","\n","   *   *","\n","   *****", "      *")
print("              *","\n","            *   *","\n","           *     *","\n","          *       *","\n","         ***     ***","\n","            *   *","\n","            *   *","\n","            *****")

#punto 21
palabra= str(input("ingrese una palabra: "))
print(palabra.replace('a','😃'))

#punto 22
frase='"El razonamiento matemático puede considerarse mas bien esquematicamente como el ejercicio de una combinacion de dos intalaciones, que podemos llamar la instuicion y el ingenio"'
print(frase[16:])

#punto 23
print("punto 23")
cadena="   El razonamiento matemático puede considerarse mas bien esquematicamente como el ejercicio de una combinacion de dos intalaciones, que podemos llamar la instuicion y el ingenio   "
sacar=cadena.strip()
print(f"{sacar}")

#punto 24
frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
palabras = frase.split()
frase_cortada = " ".join(palabras[2:])
print(frase_cortada)
frase_separada = frase_cortada[:len(frase_cortada)//2] + "\n" + frase_cortada[len(frase_cortada)//2:]
print(frase_separada)

#punto 25
print("Nombre\tEdad\tPais\tCiudad")
print("Alexa\t250\tUSA\tCapeCod")
