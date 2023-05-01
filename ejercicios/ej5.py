# 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener mejor organizado sus datos.
# a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las características que se consideren más relevantes para identificar a una persona (su nombre, DNI, edad, etc).
# b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso del estudiante y sus características (año, división, orientación, etc).
# c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad e imprimirla por pantalla
# estudiantes=[
#     {
#         "nombre":"jose",
#         "dni":123,
#         "edad":15
#     },
#     {
#         "nombre":"josefa",
#         "dni":1234,
#         "edad":16
#     },
#     {
#         "nombre":"josue",
#         "dni":12345,
#         "edad":17
#     },
#     {
#         "nombre":"josefina",
#         "dni":123456,
#         "edad":18
#     }
#     ]
# estudiantes.append({
#     "año":'', "division":'', "orientación":''
# })
    
# mayor=estudiantes[0]["edad"]
# for estudiante in estudiantes:
#     if("edad" in estudiante.keys()):
#         if(mayor<estudiante["edad"]):
#             mayor=estudiante["edad"]

# print(mayor)


# 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitiría guardar si algo es verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue esa planta a la lista de diccionarios.
# plantas=[]
# def agregarPlanta(lista,plantaInfo):
#     lista.append(plantaInfo)
# agregarPlanta(plantas,{
#     "especie":'jazmin',
#     "luzSolar":True,
#     "precio":20
# })
# print(plantas)


# 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene la siguiente información:
# Nombre del producto
# Precio por unidad
# Cantidad
# Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
# def totalMonto(ticket):
#     monto=ticket["precioUnidad"]*ticket["cantidad"]
#     return monto
# print(totalMonto({
#     "nombreProducto":'yogur',
#     "precioUnidad":50,
#     "cantidad":3
# }))


# Sol tiene una lista de diccionarios donde guarda todas las películas que vio. La información que tiene para cada una es: el nombre de la película, el año en que salió, y la puntuación que le puso del 1 al 10. Hace mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que vio. Se pide hacer una función que reciba el diccionario de las películas que vio Sol, y que devuelva una nueva lista de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.
# watchedMovies=[
#     {
#     "nombre":'alien',
#     "año":1979,
#     "puntuacion":9,
#     },
#     {
#     "nombre":'La Haine',
#     "año": 1995,
#     "puntuacion":10,
#     },
#     {
#     "nombre":'peli random',
#     "año":2025,
#     "puntuacion":6,
#     }
# ]
# def getBestOnes(movies):
#     recommended=[]
#     for movie in movies:
#         if(movie["puntuacion"]>7):
#             recommended.append(movie)
#     return recommended
# print(getBestOnes(watchedMovies))


# Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda la siguiente información:
# ● Nombre
# ● Apellido
# ● Intento
# ● Nota
# Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el primer recuperatorio y 3 si es el segundo recuperatorio.
# Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la primera oportunidad que rindieron los alumnos.
# ¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no solamente sirve para el intento 1, sino que también pueda servir para los demás.
# def promedio(notas,intento):
#     total=0
#     cant_notas=0
#     for nota_estudiante in notas:
#         if(nota_estudiante["intento"]==intento):
#             cant_notas=cant_notas+1
#             total=total+nota_estudiante["nota"]
#     return total/cant_notas
            
# notas=[
#     {
#         "nombre":"juan",
#         "apellido":"perez",
#         "intento":2,
#         "nota":3,
#     },
#     {
#         "nombre":"juann",
#         "apellido":"perezz",
#         "intento":1,
#         "nota":8,
#     },
#     {
#         "nombre":"juana",
#         "apellido":"perezzz",        
#         "intento":1,
#         "nota":3,
#     },
#     {
#         "nombre":"juanaaa",
#         "apellido":"perezeez",
#         "intento":3,
#         "nota":6,
#     },
#     {
#         "nombre":"juan7",
#         "apellido":"perez66",
#         "intento":1,
#         "nota":10,
#     }
# ]
# print(promedio(notas,2))


# 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente información de cada producto:
# ● Código del producto
# ● Fecha de vencimiento
# ● Si pasó el chequeo de calidad o no
# Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la cantidad de elementos que quedaron en el diccionario.
# Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué momento deberíamos crear la tupla?
# finalResults=[
#     {
#       "idprod":1,
#       "duedate":"june",
#       "pass":True,
#     },
#     {
#       "idprod":2,
#       "duedate":"march",
#       "pass":False,
#     },
#     {
#       "idprod":3,
#       "duedate":"june",
#       "pass":True,
#     },
#     {
#       "idprod":4,
#       "duedate":"may",
#       "pass":False,
#     },
# ]

# eliminadosIniciales=('',)
# def my_filtering_function(pair):
#     if pair["pass"]==False:
#         eliminados = eliminadosIniciales + (pair,)
#         print(f"los elementos eliminados son: {eliminados}")
#         return False
#     else:
#         return True
# productosFiltrados = list(filter(my_filtering_function, finalResults))
# print(f"quedaron {len(productosFiltrados)} elementos validos", productosFiltrados)


# Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
# a. Crear el diccionario que represente esta situación.
# AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las maratones? ¿Y qué tipo de dato es la maratón en sí?
# b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
# c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una de forma ascendente.
maratonistas = {
    "Juan": {
        "dni": 12345678,
        "maratones": [
            {"nombre": "Maratón Buenos Aires", "año": 2019, "puesto": 5, "tiempo": "2:30:15"},
            {"nombre": "Maratón Córdoba", "año": 2020, "puesto": 3, "tiempo": 2},
            {"nombre": "Maratón Rosario", "año": 2021, "puesto": 1, "tiempo": 1}
        ]
    },
    "Adolfo": {
        "dni": 23456789,
        "maratones": [
            {"nombre": "Maratón Buenos Aires", "año": 2019, "puesto": 10, "tiempo": "2:45:30"},
            {"nombre": "Maratón Córdoba", "año": 2020, "puesto": 7, "tiempo": 1},
            {"nombre": "Maratón Rosario", "año": 2021, "puesto": 3, "tiempo": 3}
        ]
    }
}
maratonistas_ordenados = sorted(maratonistas.items(), key=lambda x: x[0])
print(maratonistas)
