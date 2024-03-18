
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
print(datos_personales)

#punto 9

#punto 10

#punto 11
lista_numero=[1,2,3,4,5,6,7,8,9,10]
print(lista_numero[:3])

#punto 12
letras=['a','b','c','d','e','f','g','h','i','j']
cont=0
for i in range(len(letras)):
    i=i+2
    print(letras[:i])
    i=i+2

#punto 11
print("PUNTO 11")
mi_lista=[2,3,4,5]
print(mi_lista[::-1])

#punto 12
palabra_favorita=['Perro','Gato','Teléfono', 'Lentes','Suculentas','Termo', 'Mate', 'Café', 'Mate Cocido']
sublista=palabra_favorita[3:7]
print(sublista)
