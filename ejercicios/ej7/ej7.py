base = 'C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/'
# 111111111111111111111111111111111111 11111111111111111111111111111111111
# a = open('C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej1.txt',
#          'r', encoding='utf-8')
# text = a.readlines()
# a.close()
# archiveText = "".join(text)
# print(archiveText)
# input()


# 2222222222222222222222222222222222 2222222222222222222222222222222222222
# archivo = open(
#     'C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej2.txt', 'r', encoding='utf-8')
# personas = archivo.readlines()
# archivo.close()
# print('las personas q participan son:', "".join(personas))
# def suma_guita(lista):
#     return len(lista)*1000
# print(suma_guita(personas))
# for persona in personas:
#     if "Santi" in persona:
#         print('Santi participa')
#         edit_file = open(
#             "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej2.txt", 'a').write('\nTomas')


# print(type(personas[0]),'22')
# 33333333333333333333333333333333333 33333333333333333333333333333333333
# producto = ""
# ej3 = open(
#     "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej3.txt", 'w')
# while producto != 'X':
#     producto = input("¿Quéagregoalalistadecompras. pone X para salir")
#     if producto == 'X':
#         break
#     else:
#         ej3.write(f"{producto}\n")
# ej3.close()


# 4444444444444444444444444444444444 4444444444444444444444444444444444
# palParaReemplazar = input('a remplaz')
# reemplazarCon = input('con')
# archivo = open(
#     "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej4.txt", 'r')
# text = archivo.readlines()
# archivo.close()
# archivo_editable = open(
#     "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej4.txt", 'w')
# def aaaa(a, b):
#     for coso in text:
#         archivo_editable.write(coso.replace(a, b))
#         print(archivo)
# aaaa(palParaReemplazar, reemplazarCon)
# archivo_editable.close()


# 555555555555555555555555555555555555 555555555555555555555555555555555555
# catalogo = open(
#     'C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej5.csv', 'r')
# def leer_info():
#     info = catalogo.readlines()
#     for i in range(len(info)):
#         info[i] = info[i].strip('\n')
#         info[i] = info[i].split(';')
#     catalogo.close()
#     return info
# for productos in leer_info():
#     [name, id, price, stock] = productos
#     print('Nombre producto:', name)
#     print('Código producto:', id)
#     print('Precio producto:', price)
#     print('Stock producto:', stock)

# my_item = {
#     "nombre": "hojas A4",
#     "código": 35662,
#     "precio": 600,
#     "stock": 45
# }
# def modificar_stock(stock_dict):
#     modificar_archivo = open(
#         "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej5.csv", "a", encoding="utf-8")
#     modificar_archivo.write("\n")
#     for value in stock_dict.values():
#         modificar_archivo.write(f"{value};")
#     modificar_archivo.close()
# modificar_stock(my_item)

# 6666666666666666666666666666666666666 6666666666666666666666666666666666666
# alumnos = [{
#     "nombre": 'a',
#     "apellido": 'b',
#     "dni": 'c',
#     "nota": '3'
# },
#     {
#     "nombre": 'a',
#     "apellido": 'b',
#     "dni": 'c',
#     "nota": '7'
# },
#     {
#     "nombre": 'a',
#     "apellido": 'b',
#     "dni": 'c',
#     "nota": '9'
# }
# ]


# def agregando_notas(stock_dict):
#     modificar_archivo = open(
#         "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej6.csv", "w", encoding="utf-8")
#     for a in stock_dict:
#         modificar_archivo.write(a["nota"]+'\n')

#     modificar_archivo.close()
# def mostrar_aprobados():
#     notas_archivo = open(
#         "C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej6.csv", "r",)
#     lectura_notas = notas_archivo.readlines()
#     cont_desap = 0
#     cont_ap = 0
#     for i in lectura_notas:
#         if int(i) < 4:
#             cont_desap += 1
#         else:
#             cont_ap += 1
#     return cont_ap, cont_desap


# aprob, desap = mostrar_aprobados()
# agregando_notas(alumnos)

# 77777777777777777777777777777 77777777777777777777777777777

# def leer_info(nombre_archivo):
#     archivo = open(nombre_archivo, 'r')
#     info = archivo.readlines()
#     for i in range(len(info)):
#         info[i] = info[i].strip('\n')
#     return info


# peliculas = leer_info(f'{base}ej7.peliculas.txt')
# salas = leer_info(f'{base}ej7.salas.txt')
# nuevo_archivo = open(f'{base}ej7.funciones.csv', 'w')
# for i in range(len(peliculas)):
#     nuevo_archivo.write(f'{peliculas[i]};{salas[i]}\n')
# nuevo_archivo.close()

# 888888888888888888888888888888 888888888888888888888888888888
def leer_info(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    info = archivo.readlines()
    for i in range(len(info)):
        info[i] = info[i].strip('\n')
        info[i] = info[i].split(';')
    archivo.close()
    return info


opiniones = leer_info(f'{base}ej8.csv')


def format(data, nuevo_archivo):
    modificar_archivo = open(
        nuevo_archivo, "a", encoding="utf-8")
    # modificar_archivo.write("\n")
    # for value in stock_dict.values():
    # modificar_archivo.write(f"{value};")
    for i in range(len(data)):
        nombre, color, gusto = data[i]
        modificar_archivo.write(f'A {nombre} {gusto} le gusta el {color}\n')
        # print(f'A {nombre} {gusto} le gusta el {color}')
    modificar_archivo.close()


format(opiniones, 'C:/Users/brand/OneDrive/Escritorio/python-ej/ejercicios/ej7/ej8.format.txt')
