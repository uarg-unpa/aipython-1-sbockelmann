import random

def lanzar_dado(numero_caras):
    return  random.randint(1,numero_caras)

def lanzar_dados(cantidad, numero_caras):
    resultados = []
    for _ in range(cantidad):
        resultados.append(lanzar_dado(numero_caras))
    return resultados

def calcular_resultados(resultados):
    return sum(resultados)
    

def mostrar_estadisticas(resultados):
    minimo = min(resultados)
    maximo = max(resultados)
    promedio = sum(resultados) / len(resultados)
    print(f"Valor mínimo: {minimo}")
    print(f"Valor máximo: {maximo}")
    print(f"Promedio: {promedio}")

print("Bienvenido al Simulador de Lanzamientos de Dados")
print()
cantidad_dados = int(input("Ingrese la cantidad de dados que desea lanzar: "))
numero_caras = int(input("Ingrese el número de caras de cada dado: "))
cantidad_lanzamientos = int(input("Ingrese la cantidad de lanzamientos: "))

print()
for i in range(cantidad_lanzamientos):
    print(f" {i} lanzamiento")
    resultados = lanzar_dados(cantidad_dados, numero_caras)
    total = calcular_resultados(resultados)
    print(f"Resultados individuales: {resultados}")
    print(f"Total de los lanzamientos: {total}")
    mostrar_estadisticas(resultados)
    print()
