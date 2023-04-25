# 1.Crear una lista con los números del 1 al 10. Acceder con el índicea la posición que contiene el número 5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.
# lista=[1,2,3,4,5,6,7,8,9]
# print(lista[4])


# 2.Con la lista del punto anterior, usar la función len()para averiguar su longitud, e imprimirla.
# lista=[1,2,3,4,5,6,7,8,9]
# print(len(lista))

# 3.Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.
# lista=[2,1,3,4,5,9,8,7,6]
# print('max:',max(lista),' . ','min:',min(lista))

# 4.Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla.
# lista=[2,1,3,4,5,9,8,7,6]
# lista.sort()
# print(lista)

# 5.Crear una tupla que guarde tu nombre y tu edad. Luego,imprimir por pantalla tu edad, accediendo al elemento de la tupla que corresponda.
# person=('pepe',66)
# print(person[1])


# 6.Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
# a.Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. ¿Cómo podría saber cuál es el último elemento si no sé la longitud?
# b.Devolver el nombre que esté a dos posiciones del final.
# c.Recorrer la lista e imprimir cada nombre  por pantalla.
# d.Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición(*).
# nombres=['pepita','pepazo','pepro','Pepa','pep']
# nombres[len(nombres)-1]='jose'
# print(nombres)
# print(nombres[len(nombres)-3])
# for nombre in nombres:
    # print(nombre)
    # nombre+=' '
    # print(nombre*3)

# 7.Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación,guardarlas en una lista.
# person=('pepe',66)
# person2=('pepa',27)
# person3=('pepo',9)
# allPersons=[]
# allPersons.append(person)
# allPersons.append(person2)
# allPersons.append(person3)
# print(allPersons)



# 8.Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
# a.Crear una tupla para cada país que contenga su nombre, su capital y el continente donde seencuentra.
# b.Guardar las tuplas en una lista.
# c.Hacer una función que reciba por parámetros la lista, e imprima la información de cada paíscon el siguiente formato:País: <nombre>Capital: <capital>Continente: <continente>
# Por ejemplo: País: Japón Capital: Tokio Continente: Asia
# pais=('francia','paris','europa')
# pais2=('argentina','buenso aires','sudamerica')
# pais3=('japon','tokyo','asia')
# pais4=('alemania','berlin','europa')
# pais5=('peru','lima','sudamerica')
# paises=[pais,pais2,pais3,pais4,pais5]
# def infoPais(lista):
#     pais,capital,continente=lista
#     return f'País: {pais} \nCapital: {capital} \nContinente: {continente}'
# a=infoPais(pais2)
# print(a)

# 9.Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: [“El principito", "It", "Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
# libros=["El principito", "It", 'Sherlock Holmes',"it"]
# librosFormateados=[]
# def checkRepetidos(libroo):
#     librooLower=libroo.lower()
#     for libro in libros:
#         librosFormateados.append(libro.lower())
#     print(librosFormateados.count(librooLower))
# checkRepetidos('iT')


# 10.Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos números elevados al cuadradO
# lista=[1,2,3,4,5,6,7,8,9,10]
# listaAlCuadrado=[]
# for num in lista:
#     listaAlCuadrado.append(num*num)
# print(listaAlCuadrado)


# 11.Se tiene la siguiente lista de palabras: [“entender", "pueden", "humanos", "los", "que", "código","escriben”, ”programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código","escribe", "tonto", "Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendolas palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formarla frase.
# listaDePalabras=["entender", "pueden", "humanos", "los", "que", "código","escriben","programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código","escribe", "tonto", "Cualquier"]
# def unionReverse(lista):
#     oracion=''
#     for palab in lista:
#         oracion=palab+ ' '+oracion
#     return oracion
# print(unionReverse(listaDePalabras))

# 12.Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que vahaciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e irguardando la información en una lista hasta que ingrese una ‘X’.AYUDA: para guardar elementos nuevos en una listausamos el métodoappend().
# materias=[]
# def almacenar():
#     materia=''
#     while(not materia=='x'):
#         materia=input("que materia queres almacenar?  \ncuando no tengas q agregar mas, pone X\n")
#         materias.append(materia)
#         if(materias.count('x')):
#             materias.remove('x')
#     print(materias)
# almacenar()


# 13.Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto,precio).
# a.Hacer una función que reciba la lista y calcule y devuelva el total que hay que pagar.
# b.Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total
# ticket=(['cocacola',15],['carne',20],['chicles',2])
# ticket2=(['agua',15],['lechuga',20],['almendras',5])
# def totalPrecio(lista):
#     precioTotal=0
#     for prodPrecio in lista:
#         precio=prodPrecio[1]
#         precioTotal+=precio
#     return precioTotal
# print(totalPrecio(ticket))
# def totalPrecios(listas):
#     print(listas)
#     precioTotal=0
#     for ticket in listas:
#         for precioAndProd in ticket:
#             precio=precioAndProd[1]
#             precioTotal+=precio
#     return precioTotal
# print(totalPrecios([ticket,ticket2]))