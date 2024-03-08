#punto 1
num = 0
while num <= 100:
    print(num)
    num= num+1

#punto 2



#punto 7
nombre_usuario = str(input("Ingrese su nombre: "))
num_entero = int(input("Ingrese un número: "))
contador=1
while contador in range(num_entero):
    print(nombre_usuario)
    contador=contador+1

#punto 8


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
