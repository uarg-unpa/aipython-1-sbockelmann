#punto 6
num1 = int(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("suma es",num1+num2)
print("resta ",num1-num2)
print("Producto ",num1*num2)
print("la potencia ",num1**num2)
print("el resto",num1%num2)

#punto 9
import math
peso = float(input("ingrese su peso (en kg): "))
altura = float(input("Ingrese su altura (en metro): "))
imc= peso / altura ** 2
print( "Su índice de masa corporal es: ",imc)