# Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
# Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# Ejercicio 3
numero = int(input("Ingrese solo número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
# Ejercicio 5
contrasena = input("Ingrese contraseña entre 8 a 14 caracteres: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")
# Ejercicio 7
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    frase += "!"
print(frase)
# Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")
# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
# Ejercicio 10
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes en número (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        return "Verano"
    else:
        return "Otoño"
def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"
if hemisferio == "N":
    estacion = estacion_norte(mes, dia)
elif hemisferio == "S":
    estacion = estacion_sur(mes, dia)
else:
    estacion = "Hemisferio no válido"
print("La estación del año es:", estacion)