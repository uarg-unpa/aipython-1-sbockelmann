
#punto1
nombre=[]
print(nombre)

#punto 2
num=[1,3,4,5,6,7,8]
print(num)

#punto 3
print(len(num))

#punto 4.b
num.remove(num[0])
print(num)

#punto 4.c
num.append(20)
print(num)

#punto 5
inicio=num[0]
medios=int(len(num)/2)
medio=num[medios]
ultimo=len(num)
final=num[ultimo-1]
print(f"inicio: {inicio}; medio: {medio}; final: {final}")

#punto 6
datos_personales=['Susana Bockelmann', 36, 1.73, 'Soltera', 'Roque Saenz Peña 554']

#punto 7.a
compañia=['Facebook', 'TikTok', 'X', 'Claro','Movistar']
print(compañia)

#punto 7.b
for j in range(len(compañia)):
    print(j,  compañia[j])

#punto 7.c
    
#punto 8
lista_numero=[1,2,3,4,5,6,7,8,9,10]
print(lista_numero[:3])


#punto 9
letras=['a','b','c','d','e','f','g','h','i','j']
cont=0
for i in range(len(letras)):
    i=i+2
    print(letras[:i])
    i=i+2

#punto 10
mi_lista=[2,3,4,5]
print(mi_lista[::-1])

#punto 11
print("PUNTO 11")
palabra_favorita=['Perro','Gato','Teléfono', 'Lentes','Suculentas','Termo', 'Mate', 'Café', 'Mate Cocido']
sublista=palabra_favorita[1:4]
print(sublista)

#punto 12
flores=['rosas', 'orquídea','lirio','tulipan', 'margarita', 'dalia', 'hortensia']
#punto 12.a
tercer_elemento=flores[2:5]
print(f"a. Mostrar tres elementos desde el tercer elemento: {tercer_elemento}" )
#punto 12.b
print("b. Elementos en posiciones pares desde la segunda posición:", flores[1::2])
#punto 12.c
print("c. Todos los elementos desde la primera posición saltando de a tres elementos:", flores[::3])


#punto 13
def contar_vocales(lista_caracteres):
    vocales="aeiouAEIOU"
    cantidad_vocales=0
    for caracter in lista_caracteres:
        if caracter in vocales:
            cantidad_vocales=cantidad_vocales+1
    return cantidad_vocales
lista_caracteres = ['a', 'r', 'e', 'k', 'o', 'E', 'A', 'U']
cantidad = contar_vocales(lista_caracteres)
print(f"La lista tiene {cantidad} vocales.")

#punto 14
def intercalar_listas(lista1, lista2):
    lista_resultante=[]
    longitud_maxima=max(len(lista1), len(lista2))
    for i in range(len(lista1)):
        if i < len(lista1):
            lista_resultante.append(lista1[i])
        if i < len(lista2):
            lista_resultante.append(lista2[i])
    return lista_resultante
lista1 = ['a', 'b', 'c','d','e','f','g']
lista2 = [1, 2, 3,4,5,6]
nueva_lista = intercalar_listas(lista1, lista2)
print(nueva_lista)

#punto 15
def promedio(lista_numero):
    suma=0
    promedio=0
    for j in range(len(lista_numero)):
        suma=suma+lista_numero[j]
    promedio= suma/len(lista_numero)
    return promedio
lista_numero=[1,2.3,5,10,11]
resultado_promedio=promedio(lista_numero)
print(f"El promedio de la lista número es: {resultado_promedio} ")