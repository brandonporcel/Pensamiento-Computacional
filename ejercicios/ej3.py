# Expresiones##########################################################
# 1. Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo bool e imprimirla por pantalla para ver su valor.
# def bigger(n1,n2):
#     bigger=n1>n2
#     return bigger
# print(bigger(2,4))


# 2. Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
# vocales=["a",'e','i','o','u']
# def checkVocal(letter):
#     for vocal in vocales:
#         rta=True if letter==vocal else False
#         return rta
# print(checkVocal(input("ingresa una letra en minuscula mi amigo y te voy a decir es es vocal o no: ")))


# 3. Repetir pero para la expresión que permite saber si un número es par y menor a 10.
# def checkNum(num):
#     res=num%2==0 and num<10
#     return res
# userNum=int(input("ingresa un numero y te voy a decir es es par Y menor a 10 o no: "))
# print(checkNum(userNum))



# Estructuras de control condicionales%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# 4. Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es el mismo número sin considerar el signo.
# Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4).
# def checkAbs(num):
#     pos=num if num>0 else num*(-1)
#     return pos
# print(checkAbs(-52))

# 5. Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va a ser representado con una letra: R para piedra, P para papel y S para tijera.
# a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
# la jugada para ganarle. Por ejemplo:
# > ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
# > P
# > Tijera. ¡Te gané!
# ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
# que hacer (en este caso ingresar alguna de las tres letras).
# b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
# (distinta de R, P o T).
# def rPSGame(mov):
#     if(mov=="R"):
#         return "Papel. ¡Te gané!"
    # elif(mov=="P"):
    #     return "Tijeras. ¡Te gané!" 
    # elif(mov=="S"):
    #     return "Piedra. ¡Te gané!" 
    # else:
    #     return "No vale, Sacaste la mano despues"
# userMov=input("ingresa una letra siendo R para piedra, P para papel y S para tijera y te voy a ganar: ")
# print(rPSGame(userMov))


# 6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?.
# def checkNum(num,num2,lim):
#     sum=num+num2
#     message=""
#     if(sum<lim):
#         message=f"para llegar a {lim} faltan {lim-sum}!"
#     else:
#         message=f"tu num llega a {lim}!!!"    
#     return message
# userNum=int(input("ingresa un numero, campeon/a: "))
# userNum2=int(input("ingresa un numero, campeon/a: "))
# userLim=int(input("queres sabes a cuanto esta tu num a x distancia? ponelo: "))
# print(checkNum(userNum,userNum2,userLim))


# 7. Se tienen letras para representar las estaciones del año:
# ● V para verano
# ● O para otoño
# ● I para invierno
# ● P para primavera
# Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O, B, V e I.
# def checkSeason(letter):
#     seasons=["verano","otoño","invierno","primavera"]
#     for i in range(0, len(seasons)):
#         if(letter==seasons[i][0:1].upper()):
#             return seasons[i]
#         elif(i==len(seasons)-1 and letter!=seasons[i][0:1].upper()):
#             return "error"
# print(checkSeason("A"))
# print(checkSeason("P"))



# Estructuras de control iterativas ))))))))))))))))))))))))))))))
# 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control iterativa for.
# def untilOperation(num):
#     for i in range(1,num+1):
#         print(i)
# userNum=int(input("ingresa un numero: "))
# untilOperation(userNum)


# 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10.
# def mult(num):
#     for i in range(1,11):
#         print(i*num)
# userNum=int(input("ingresa un numero: "))
# mult(userNum)


# 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces.
# def fc(num):
#     i=0
#     while(i<num):
#         print("feliz cumple cumpa")
#         i+=1
# userNum=int(input("ingresa un numero: "))
# fc(userNum)


# 11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
# Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
# > El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
# > 10
# > El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
# > 15
# > El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
# > 5
# def cobro(totalCompra):
#     loQuePago=0
#     cobranzaMomentania=0
#     while(cobranzaMomentania>=0):
#         monto=int(input("cuanto vas a abonar: "))
#         loQuePago+=monto
#         cobranzaMomentania=totalCompra-loQuePago
#         print(f"El importe a pagar es de {cobranzaMomentania} pesos. Por favor, ingrese un monto")
# cobro(50)



# Estructuras de control condicionales e iterativas$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar, imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
# > El número 1 es impar.
# > El número 2 es par.
# …
# > El número 20 es par.
# def checkPar():
#     for i in range(1,21):
#         if(i%2==0):
#             print(f"el numero {i} es par")
#         else:
#             print(f"el numero {i} no es par")
# checkPar    ()


# 13. Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de fichas, y se quiere hacer una función que imite ese comportamiento.
# a. Hacer una función que reciba un número que represente el precio de la máquina, e imprima por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las fichas necesarias. Por ejemplo, si la función recibe 3, debería tener el siguiente comportamiento:
# > Ingresá 3 fichas para comenzar
# > F
# > Ingresá 3 fichas para comenzar
# > F
# > Ingresá 3 fichas para comenzar
# > B
# > Ingresá 3 fichas para comenzar
# > F
# > ¡A jugar!
# ATENCIÓN: notar cómo cuando se ingresa una letra distinta de F, esta se ignora a la hora de contar la cantidad de fichas que fueron ingresadas.
# def empezar_jugada(cant_fichas):
#     fichas_ingresadas=0
#     while(fichas_ingresadas<cant_fichas): 
#         print(f"ingresa {cant_fichas} fichas para comenzar")
#         letra=input()
#         if(letra=="F"):
#             fichas_ingresadas=fichas_ingresadas+1
# empezar_jugada(3)        


# b. Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN ingresar para empezar a jugar Es decir:
# > Ingresá 3 fichas (F) para comenzar
# > F
# > Ingresá 2 fichas (F) para comenzar
# > F
# > Ingresá 1 fichas (F) para comenzar
# > B
# > Ingresá 1 fichas (F) para comenzar
# > F
# > ¡A jugar!
# def cuantasFaltan(cant_fichas):
#     fichas_ingresadas=0
#     fichasCorrectas=0
#     while(fichas_ingresadas<cant_fichas): 
#         print(f"ingresa {cant_fichas-fichasCorrectas} fichas para comenzar")
#         letra=input()
#         if(letra=="F"):
#             fichas_ingresadas+=1
#             fichasCorrectas+=1
# cuantasFaltan(3)


# c. Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)” cuando se recibe una letra distinta de F.
# def cuantasFaltan(cant_fichas):
#     fichas_ingresadas=0
#     fichasCorrectas=0
#     while(fichas_ingresadas<cant_fichas): 
#         print(f"ingresa {cant_fichas-fichasCorrectas} fichas para comenzar")
#         letra=input()
#         if(letra=="F"):
#             fichas_ingresadas+=1
#             fichasCorrectas+=1
#         else:
#             print('Por favor solamente ingrese fichas reales (F)')
# cuantasFaltan(3)


# 14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número ingresado.
# AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea distinto de 0, o sea que no sea divisible.
# esta mal, no se como hacerlo :p
# def checkPrimo(num):
#     for i in range(0, num):
#         if (num %i)==0:
#             print(f"{i} es un numero primo")
# userNum=int(input("ingresa un num compi: "))
# checkPrimo(userNum)


