#punto 1
edad = int(input('Ingrese su edad: '))
if edad >= 18:
    print("Tiene edad suficiente para conducir")
else:
    falta=18 - edad
    print(f"le falta {falta} años para poder conducir") 

#punto 2
edad_usuario = int(input("Ingrese su edad: "))
mi_edad = 36
if mi_edad > edad_usuario:
    print("Soy mayor que tú")
    diferencia = mi_edad - edad_usuario
    if diferencia == 1:
        print(f"Te llevo {diferencia} año de ventaja")
    else:
        print(f"Te llevo {diferencia} años de ventaja")
elif mi_edad < edad_usuario:
    print("Eres mayor que yo")
    diferencia = edad_usuario - mi_edad
    if diferencia == 1:
        print(f"Me llevas {diferencia} año de ventaja.")
    else:
        print(f"Me llevas {diferencia} años de ventaja.")
else:
    print("¡Somos de la misma generación! ¡Qué coincidencia!")

#punto 3
contraseña_guardada = "Contraseña123"
contraseña_usuario = input("Ingrese su contraseña: ")
if contraseña_guardada.lower() == contraseña_usuario.lower():
    print("¡La contraseña es correcta!")
else:
    print("La contraseña no coincide.")

#punto 4
a = float(input("ingrese un número: "))
b = float(input("ingrese el segundo número: "))
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

#punto 5
num = int(input("ingrese un número: "))
if num % 2 == 0:
    print(f"El número {num} es par")
else:
     print(f"El número {num} es impar")

#punto 6
semana=int(input("Ingrese un número del 1 al 7"))
if semana >= 1 and semana <=7:
    match semana:
        case 1:
            print("lunes")
        case 2:
            print("martes")
        case 3:
            print("miercoles")
        case 4:
            print("jueves")
        case 5:
            print("viernes")
        case 6:
            print("sabado")
        case 7:
            print("domingo")
else:
    print(f"El número {semana} no se encuntra dentro del rango del 1 al 7")

#punto 7
puntaje= int(input("Ingrese su puntaje: "))
if (puntaje >= 80 and puntaje <= 100):
    print("A")
elif puntaje >=70 and puntaje <=89:
    print("B")
elif puntaje >=60 and puntaje <=69:
    print("C")
elif puntaje >=50 and puntaje <=59:
    print("D")
else:
    print("F")

#punto 8
edad_usuario1=int (input("Ingrese la edad del cliente: "))
if edad_usuario1 < 4:
    print("puede pasar gratis")
elif edad_usuario1 > 4 and edad_usuario1 <8:
    print("Debe pagar $5")
else:
    print("Debe pagar $10")

#punto 9
edad_usuario = int(input("Ingrese la edad: "))
ingreso = int(input("Ingrese su ingreso mensual: "))
if edad_usuario >= 18 and ingreso >= 100000:
    print("Tiene que pagar impuestos")
else:
    print ("No tiene que pagar inpuestos")

 