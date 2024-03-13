#punto 1
def multiplicacion (num1,num2):
    return (num1*num2)

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el primer número: "))
print(multiplicacion(num1,num2))

#punto 2
def multiplicacion1 ():
    return (1*1)

print(multiplicacion1())

#punto 3

def nombres(nombre):
    print("Aguante la programación ...")

nombres(nombre="Susana")

#punto 4
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}", end="\n")
    print()

numero = int(input("Ingresa un número: "))
tabla_multiplicar(numero)

#punto 5
def paroimpar(numer):
    if(numer%2 ==0 ):
        print(f"El número {numer} es PAR")
    else:
        print(f"El número {numer} es IMPAR")

numer=int(input("Ingrese un número para calcular par o impar: "))
paroimpar(numer)

#punto 6
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#punto 7
def maximo (numero1,numero2, numero3):
    return max(numero1,numero2,numero3)

numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
numero3=int(input("Ingrese el tercer número: "))
resultado=maximo(numero1,numero2,numero3)
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es {resultado}")

#punto 8
def invertir(palabra):
    return palabra[::-1]

palabra=str(input("Ingrese una palabra para luego ser invertida: "))
resul=invertir(palabra)
print(f"La palabra invertida es: {resul}")

#punto 9
def palindromo(palabras):
    palabras = palabras.lower().replace(" ", "")
    return palabras == palabras[::-1]
    
palabras=str(input("Ingrese la palabra que desea saber si es palídromo: "))
if palindromo(palabras):
    print(f"'{palabras}' es un palíndromo.")
else:
    print(f"'{palabras}' no es un palíndromo.")

#punto 10
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperatura_fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} grados Fahrenheit son equivalentes a {temperatura_celsius} grados Celsius.")