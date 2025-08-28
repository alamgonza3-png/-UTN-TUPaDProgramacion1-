# -UTN-TUPaDProgramacion1-
#ejercicio 1
print ("hola mundo")
#ejercicio 2
nombre = input ( " ingrese su nombre " )
print (f"hola {nombre}")
#ejercicio 3
nombre =input ("ingrese su nombre ")
apellido =input ("ingrese su apellido ")
edad =input ("ingrese edad ")
pais =input ("ingrese pais donde vive " )
print (f" hola, soy {nombre} {apellido},tengo {edad}, vivo en {pais} ")
#ejercicio 4
import math
radio_circulo = float(input("por favor ingrese radio de un circulo " ))
area_circulo =  math.pi * (radio_circulo) ** 2 
perimetro_circulo = 2 * math.pi * radio_circulo
print (f"el area del circulo es {area_circulo} y el perimetro es de {perimetro_circulo}")
#ejercicio 5
segundos = float (input("ingresar una cantidad de segundos para convertirlo en horas "))
horas =  round ( segundos // 3600 , 2 )
print (f" los segundos ingresados ,{segundos}, equivale a {horas} ")
#ejercicio 6
numero = int(input("Ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
#ejercicio 7
numero1_suma = int (input ("ingrese 1er numero para sumar "))
numero2_suma = int(input ("ingrese 2do numero para sumar "))
numero1_resta= int(input("ingrese 1er valor para restar "))
numero2_resta= int(input("ingrese 2do valor para restar "))
numero1_multiplicacion =int (input ("ingrese un 1er para muliplicar "))
numero2_multiplicacion = int(input ("ingrese un 2do para muliplicar "))
numero1_division = float(input ("ingrese 1er numero para dividir "))
numero2_division = float(input ("ingrese el 2do numero para dividir "))
suma = numero1_suma + numero2_suma
resta = numero1_resta - numero2_resta
division = round (numero1_division / numero2_division , 2 )
multiplicacion = numero1_multiplicacion * numero2_multiplicacion
print (f"la suma de los dos numeros ingresados son {numero1_suma} + {numero2_suma} = {suma}" )
print (f"la resta de los dos numeros ingresados son {numero1_resta} - {numero2_resta} = {resta}" )
print (f"la division de los dos numeros ingresados son {numero1_division} % {numero2_division} = {division}" )
print (f"la multiplicacion de los dos numeros ingresados son {numero1_multiplicacion} x {numero2_multiplicacion} = {multiplicacion}" )
#ejercicio 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros (ejemplo: 1.75): "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc:.2f}")
#ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
#ejercicio 10
numero1 = int (input("ingrese 1er numero a promediar "))
numero2 = int (input("ingrese 2do numero a promediar "))
numero3 = int (input("ingrese 3er numero a promediar " ))
promedio =  float(numero1 + numero2 + numero3) / 3
print (f"el promedio es {promedio}% ") 