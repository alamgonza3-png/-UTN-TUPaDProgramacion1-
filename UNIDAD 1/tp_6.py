1#
def imprimir_hola_mundo():
    print ("hola mundo")
imprimir_hola_mundo()
2#
def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"
nombre = input ("ingrese su nombre ")
saludo = saludar_usuario(nombre)
print (saludo)
3#
def informacion_personal (nombre, apellido, edad, residencia):
    print (f"soy {nombre} {apellido} , tengo {edad} aÑos, vivo en {residencia}.")

nombre = input ("ingresar tu nombre " )
apellido = input ("ingresar apellido " )
edad = input ("ingresar edad " )
residencia = input ("ingresad localidad donde vive " )
informacion_personal(nombre,apellido,edad,residencia)
4#
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
5#
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = float(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.1f} horas.")
6#
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)
8#
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.1f}")
9#
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
10#
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio:.2f}")