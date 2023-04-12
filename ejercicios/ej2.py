#EJERCICIOS SEMANA 2

#1. Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.
# num=int(input("ingrese un num: "))
# print(num)


# 2. Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
# ● la suma de ambos números
# ● la resta de ambos números
# ● la multiplicación de ambos números
# ● la división entera de ambos números
# ● el resto
# num1,num2=input("ingrese un num: "), input("ingrese otro num: ")

# def calc(n1,n2,operation):
#     return eval(n1+operation+n2)

# operationn= input('Operador (+ - * / // % ): ')
# result=calc(num1,num2,operationn)
# print(result)



#3. Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un mensaje que indique el resultado.
# userNum=int(input("ingrese un num: "))
# if (userNum%2==0):
#     print(f"{userNum} es par")
# else:
#     print(f"{userNum} NO es par")



# 4. Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía el usuario en el año ingresado.
# userNum=int(input("ingrese tu año de nacimiento: "))
# userNum2=int(input("cuantos años vas a tener en el año: "))
# if(userNum2<=userNum): 
    # userNum2=input("no podes poner un año menor-igual al de tu nacimiento, ingresa otro: ")
# else:    
    # print(userNum2-userNum)



# 5. Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
# user_input =input("Ingrese 5 números, separados por espacios: ")
# nums = user_input.split(" ")
# sum=0
# for val in nums:
    # sum+=int(val)
# print(round(sum/len(nums)))

# n=int(input('cant de num a promediar: '))
# suma=0
# iteration=1
# while(iteration<=n):
    # nota=int(input('numero a prom: '))
    # suma+=nota
    # iteration+=1
# prom=suma / n
# print(prom)



# 6. Crear una función que reciba un número y muestre el anterior y el siguiente.
# def c():
#     a=int(input("ingresa un num: "))
#     print(a-1,a,a+1)
# c()


# 7. Crear una función que una un string y un entero.
# def conc(strr,num):
    # print(strr+str(num))
# conc("2",2)


# 8. Crear una función que reciba dos enteros y que retorne el resto y el cociente.
# def calc(n1,n2):
    # coc=n1/n2
    # res=n1%n2
    # return coc,res
# coc,res=calc(8,4)
# print(coc,res)



# 9. Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.
# def conc(nom,ap):
    # print(f"{nom} {ap}!!")
# conc("jose", "perez")



# 10. Obtener una palabra e imprimir la cantidad de letras.
# def cant(text):
    # print(len(text))
# cant("jose")



# 11. Obtener una palabra e imprimir los primeros 5 caracteres.
# def cant(text):
    # print(text[0:5])
# cant("paradela")



# 12. Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla.
# palabra=input('ingresa una palabra: ')
# arrPalabra= list(palabra)
# palabraModif=[]
# for val in arrPalabra:
#     if(val!="a"):
#         palabraModif.append(val)
# palabraModif="".join(palabraModif)
# print(palabraModif)

# print(palabra.replace("a",''))