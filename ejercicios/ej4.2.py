# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
# def imprimir_vocales(string):
#     vocales = "aeiouAEIOU"
#     newWord=''
#     for letra in string:
#         if letra in vocales:
#             newWord+=letra
#     return newWord
# print(imprimir_vocales("Hola mundo"))


# 2. Hacer una función que reciba un string y que lo invierta.
# def invertir(string):
#     print(string[::-1])
# invertir("Hola mundo")


# 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo. Se pide devolver el string habiendo eliminado el substring del mismo.
# def removeSub(string,substring):
#     if(substring in string):
#         a=string.replace(substring,'')
#     print(a)
# removeSub('messi','ssi')


#4. Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo quiere agregar un ingrediente a la lista sin que lo haya escrito antes, así no +tiene repetidos. Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento que se desea insertar no se encuentra en la lista.

# lista=['pepino','carne','aceite']
# def checkRepetido(ingrediente):
#     if(ingrediente in lista):
#        print('el ingrediente ya esta en la lista')
#        return
#     lista.append(ingrediente)
#     print(lista)
# nuevoIngrediente=input('ingresa tu nuevo ingrediente: ')
# checkRepetido(nuevoIngrediente)


# 5. Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su mano en el lugar indicado para no romper el orden. Si tiene una lista de enteros ordenadas de mayor a menor, hacer una función que según esa lista inserte un nuevo entero, manteniendo el orden. ¿En este caso nos conviene usar append?

# cartas=[1,4,6,5,8,9]
# cartas.sort()
# userNum=int(input('pon un numero canaya'))
# for carta in cartas:
#     if(userNum < carta):
#         position=cartas.index(carta)
#         # print(cartas.index(carta))
#         cartas.insert(position,userNum)
#         break
#     elif userNum in cartas:
#         print('el numero ia esta en elkmazo bro')
#         break
#     continue
    
        
# nuevaCarta(8)
# print(cartas)

# Santiago armó una lista con el pedido de empanadas de su familia,  pero ahora quiere saber la cantidad de gustos diferentes que tiene que pedir.  Hacer una función que según una lista de strings elimine todos los elementos repetidos y devuelva su tamaño.
# lista=['carne','pollo','pollo','salteñas','humita','humita']
# listaFormateada=[]
# def eliminarRep(listaa):
#     listaFormateada=set(listaa)
#     return len(listaFormateada)
# print(eliminarRep(lista))


# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa. Decidieron dividirse las tareas, a Manu le tocó hacer todas las actividades con número par. Hacer una función que reciba una lista de enteros y devuelva otra lista que solamente contenga números pares.
# lista=[1,2,3,4,5,6,7,8]
# par=[]
# impar=[]
# def separar(listaa):
#     for i in range(1,len(listaa)):
#         if(i%2==0):
#             par.append(i)
#         else:
#            impar.append(i)
# separar(lista)
# print(par,impar)


# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados.  Cada uno tiene su propia tupla y guarda en ella a todos los que quiere invitar. 
# 8. Si alguien cancela tienen que sacarlo de la tupla. 
# Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado por parámetro. 
# Las tuplas son inmutables, entonces ¿cómo podemos hacer para “eliminar” un elemento de una tupla?
# invitados=('jose','josefina','jero')
# nueva_tupla=()
# def eliminar_elemento(tupla, invitado):
#     nueva_tupla = tuple(filter(lambda invitadoDeLista: invitadoDeLista != invitado, tupla))
#     return nueva_tupla
# nueva_lista = eliminar_elemento(invitados, 'jose')
# print(nueva_lista)  


# Cuando ya tienen a todos los invitados tienen que juntar sus tuplas. Hacer una función que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.

# invitados=('jose','josefina','jero')
# invitados2=('josue','jacinto','jaz')

# def sumarTuplas(t1,t2):
#     nuevaTupla=t1+t2
#     return nuevaTupla
# print(sumarTuplas(invitados,invitados2))



