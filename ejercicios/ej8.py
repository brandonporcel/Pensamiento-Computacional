import pandas as pd
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

# Mostrar la información del DataFrame con el método info(), ¿Cómo se llaman y qué tipo de dato tiene cada columna? ¿Cuántos elementos nulos hay en cada columna? Interpretar qué información se guarda en esta tabla y para qué puede servir.
df.info()

# Mostrar sólo los nombres de las primeras 3 películas del DataFrame.
df.head(3)["nombre"]

# Mostrar sólo el director y el género de todas las películas.
df[["nombre", "director"]]

# Mostrar las películas que sean de drama
cond = df["género"] == "drama"
df[cond]

# ¿Qué cantidad de películas hay de cada género?
df["género"].value_counts()

# Mostrar las películas que tengan puntaje entre 6 y 8 y cuyo año de estreno sea anterior a los 2000
cond = df["puntaje"].between(6, 8) & (df["año"] < 2000)
df[cond]

# Mostrar las películas que no hayan sido puntuadas (que el puntaje tenga un valor nulo).
c = df["puntaje"].isnull()
df[c]

# Calcular el promedio del puntaje de todas las películas.
df["puntaje"].mean()

# Ordenar las películas en orden alfabético descendente.
df.sort_values(by="nombre", ascending=False)

# Mostrar las 3 películas más antiguas.
df.sort_values(by="año", ascending=True).head(3)

# Mostrar sólo el nombre y el año de las 3 películas más nuevas.
df.sort_values(by="año", ascending=False).head(3)[["nombre", "año"]]

# Agregar una columna que indique si la película fue vista, o no. Una película fue vista cuando tiene puntaje no nulo
df["vista"] = df["puntaje"].notnull()
df["vista"] = df["vista"].replace(True, 'si')
df["vista"] = df["vista"].replace(False, 'no')
