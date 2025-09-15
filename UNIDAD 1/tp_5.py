#1
for i in range(0, 101, 4 ):
    print(i)
2#  
letras= ['a','b','c','d','e']
print (letras[3])
#3
saludos=[]
saludos.append("hola")
saludos.append("buenos dias")   
saludos.append("como estas?")
print (saludos)
4#
animales = ["perro", "gato", "conejo", "pez"]
animales [1] = "loro"
animales [3] = "oso"
print (animales)
5#
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print (numeros  )  
"lo que este codigo hace es eliminar el numero mayor de la lista"
6#
numeros = list(range(10, 31 , 5))
print (numeros[:2])
7#
autos = ["sedan", "polo", "suran", "gol"]
autos [1] = "toyota"
autos [2] = "ford"
print (autos)
8#
lista =[5,10,15]
dobles = []
for numero in lista:
    dobles.append (numero * 2)
print (dobles) 
9#
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append  ("jugo")
compras [1] [1] = "tallarines"
compras [0].remove("pan")
print (compras)
10#
lista_anidada = [15,True,[25.5,57.9,30.6],False]
print (lista_anidada) 