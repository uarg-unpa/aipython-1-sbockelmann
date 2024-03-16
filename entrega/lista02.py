#crear una lista usando un metodo
#nombres=list()
#crear una lista con valores iniciales
nombres=list(['Gaston', 'Eva', 'Lautaro'])
#print(nombres)
#metodos, append, permite agregar una elemento al final de la lista
nombres.append('Sandra')
#print(nombres)
#vampoos a utlizar la funcion id
print(id(nombres))
for nombre in nombres:
    print(nombre)
#inset
nombres.insert(0,'Victoria')
#print(nombres)
#utilizar el operador in
for nombre in nombres:
    print(nombre)
#mutabilidad
print()
nombres[4]='Loreza'
for nombre in nombres:
    print(nombre)
print(id(nombres))


