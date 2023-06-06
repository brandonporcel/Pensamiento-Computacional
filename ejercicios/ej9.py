import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Graficar la función f(x)=x*x*x. Pueden usar de ejemplo el apunte donde está graficada la función f(x)=x*x.
x = list(range(-10, 11))
# y=i**3 (i for x)
y = [number**3 for number in x]
plt.plot(x, y)
plt.ylabel("yyy")
plt.show()


# La siguiente lista contiene las temperaturas en celsius a lo largo del día medidas cada 30 minutos:
temperaturas = [15, 16, 16, 17, 16, 15, 14, 14, 14, 15, 16, 15, 15, 16, 15, 14, 13,
                12, 12, 12, 12, 13, 14, 15, 16, 17, 18, 18, 18, 18, 18, 18, 18, 17,
                17, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# El primer elemento corresponde a la temperatura a las 00:00 y la última a las 23:30. Realizar un gráfico que tenga en el eje X la hora y en el eje Y la temperatura. Darle un título y anotar que representa cada eje.
horas = [0]
hora_1 = 0
while hora_1 < 23.5:
    hora_1 += .5
    horas.append(hora_1)
plt.plot(horas, temperaturas)
plt.ylabel("temperatura")
plt.xlabel("tiempo")
plt.show()


# Usando el set de datos de películas de la guía de ejercicios de pandas. Hacer un gráfico de barras que muestre la cantidad de películas de cada género.
peliculas = {'nombre': ['Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
                        'Casablanca', 'El exorcista',  'Soy leyenda',
                        'El club de la pelea', 'Mujercitas'],
             'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
                          'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
                          'William Friedkin', 'Francis Lawrence', 'David Fincher',
                          'Greta Gerwig'],
             'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
             'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
                         'ciencia ficción', 'drama', 'drama'],
             'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0],
             'vista': ['si', 'no', 'si', 'si', 'si', 'si', 'no', 'no', 'si', 'si']}

df = pd.DataFrame(peliculas)

y = df["género"].value_counts()
# list(y.keys())
plt.bar(y.keys(), y.tolist())


# Usando el set de datos de películas de la guía de ejercicios de pandas. Hacer un gráfico de torta que muestre la proporción de películas vistas y no vistas.
y = df["género"].value_counts()
nombres = y.keys()
plt.pie(y, labels=nombres)
plt.show()


# Dado el siguiente set de datos misterioso que contiene una serie de puntos con formato (x,y):
puntos = [(0.3, 0.46),
          (0.3286, 0.4176),
          (0.3571, 0.3816),
          (0.3857, 0.3522),
          (0.4143, 0.3294),
          (0.4429, 0.3131),
          (0.4714, 0.3033),
          (0.5, 0.3),
          (0.5286, 0.3033),
          (0.5571, 0.3131),
          (0.5857, 0.3294),
          (0.6143, 0.3522),
          (0.6429, 0.3816),
          (0.6714, 0.4176),
          (0.7, 0.46),
          (0.35, 0.63),
          (0.65, 0.63),
          (0.5, 0.5)]
# Hacer un gráfico de dispersión que muestre todos los puntos.
# [number**3 for number in x]
x = [s[0] for s in puntos]
y = [s[1] for s in puntos]
plt.xlabel('X')
plt.ylabel('Y')
plt.title("puntos sueltos")
plt.scatter(x, y)
plt.show()
