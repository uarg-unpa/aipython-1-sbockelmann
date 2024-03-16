#punto 6
num1 = int(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("suma es",num1+num2)
print("resta ",num1-num2)
print("Producto ",num1*num2)
print("la potencia ",num1**num2)
print("el resto",num1%num2)

#punto 8
base= float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
print("El perimetro es: ",2*altura+2*base)
print("El area del rectangulo es: ",base*altura)

#punto 9
import math
peso = float(input("ingrese su peso (en kg): "))
altura = float(input("Ingrese su altura (en metro): "))
imc= peso / altura ** 2
print( "Su índice de masa corporal es: ",imc)

#punto 10
celsius = float(input("Ingrese la termpera Celsius: "))
fahrenheit= celsius * 9/5 + 32
print(f"La trasformación de grados celsius a Fahrenheit es: {fahrenheit} ")

#punt11
hora_trabajada = int(input("Ingrese el número de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo por hora: "))
print("El sueldo que le corresponde es", hora_trabajada*costo_por_hora)

#punto 12
cantidad = int(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Interes anual es: "))
años = int(input("Número de años: "))
capital_obtenido = cantidad * (1 + interes_anual) ** años
capital_obtenido = round(capital_obtenido, 2)
print(f"el capital obtenido de inversion es: {capital_obtenido}")
