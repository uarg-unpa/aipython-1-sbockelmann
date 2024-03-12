#punto 1
num = 0
while num <= 100:
    print(num)
    num= num+1

#punto 2
for i in range(0, 100):
    print(i, end=' ')
#punto 3
num = 10
while num >= 0:
    print(num, end=' ')
    num -= 1
print("FOR.....")
for i in range(10, -1, -1):
    print(i, end=' ')
#punto 4
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
if num1 < num2:
    start_num = num1
    end_num = num2
else:
    start_num = num2
    end_num = num1
cont_num = start_num + 1
while cont_num <end_num:
    print(cont_num, end=' ')
    cont_num += 1

#punto 5
for i in range(1, 8):
    print("#" * i)

#punto 6
for i in range(7):
    for j in range(8):
        print("#", end="")
    print()

#punto 7
nombre_usuario = str(input("Ingrese su nombre: "))
num_entero = int(input("Ingrese un número: "))
contador=1
while contador in range(num_entero):
    print(nombre_usuario)
    contador=contador+1

#punto 8
num = int(input("Ingrese un número entero positivo mayor a 3: "))
if num <= 3:
    print("El número ingresado no es válido.")
else:
    print("Números impares hasta", num, ":")
    for i in range(1, num + 1, 2):
        print(i)

#punto 9
cont = int(0)
while cont <= 10:
    multiplicacion=cont*cont
    print(cont,"x",cont," = ",multiplicacion)
    cont=cont+1

#punto 10
for i in range(7):
    for j in range(i, 7):
        print(f"{i} {j}")

#punto 11
num = int(input("Ingrese un número entero: "))
for i in range(1, num+1, 2): # 1 es como comienza; num+1 es el incremento; 2 es el aumento
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()

#punto 12
n = int(input("Ingrese un número: "))
suma=0
expresion = ""
for i in range(1,n+1):
        suma += i
        expresion +=str(i)
        if i < n:
            expresion += " + "
        else:
            expresion += " = "
print(expresion + str(suma))

#punto 13
N = int(input("Ingrese un número: "))
suma_pares=0
for i in range (1,N+1):
    if i % 2 == 0:
        suma_pares = suma_pares+i
print(f"La suma de los primeros {N} número pares es {suma_pares}")

#punto 14
num1 = int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
if num1 > num2:
    num1,num2 =num2,num1 #Intercambia los valores si el primero es mayor que  el segundo
print(f"Números paresentre {num1} y {num2} son:")
for k in range(num1, num2,+1):
    if(k%2==0):
        print(k)

#punto 15
num = int(input("Ingrese un número entero positivo mayor a 1: "))
es_primo = True
if num <= 1:
    es_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
