1#
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
2#
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)
3#
frutas = list(precios_frutas.keys())
print(frutas)
4#
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = telefono
consulta = input("Ingrese el nombre del contacto que desea buscar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"No se encontró un contacto con el nombre {consulta}")
5#
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Palabras únicas:", palabras_unicas)
print("Cantidad de veces que aparece cada palabra:", contador_palabras)
6#
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas_str = input(f"Ingrese las 3 notas de {nombre} separadas por espacios: ")
    notas = tuple(map(float, notas_str.split()))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")
#7
parcial1 = {'Ana', 'Luis', 'Carla', 'Jorge'}
parcial2 = {'Luis', 'Carla', 'Marta', 'Pedro'}
ambos = parcial1.intersection(parcial2)
print("Estudiantes que aprobaron ambos parciales:", ambos)
solo_uno = parcial1.symmetric_difference(parcial2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)
total = parcial1.union(parcial2)
print("Lista total de estudiantes que aprobaron al menos un parcial:", total)
8#
stock_productos = {
    'manzana': 10,
    'banana': 5,
    'naranja': 8
}
while True:
    print("\nOpciones:")
    print("1 - Consultar stock")
    print("2 - Agregar unidades a un producto existente")
    print("3 - Agregar un nuevo producto")
    print("4 - Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ").lower()
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]} unidades.")
        else:
            print(f"El producto {producto} no existe en el stock.")

    elif opcion == '2':
        producto = input("Ingrese el nombre del producto al que desea agregar unidades: ").lower()
        if producto in stock_productos:
            try:
                unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
                if unidades > 0:
                    stock_productos[producto] += unidades
                    print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades.")
                else:
                    print("Debe ingresar un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print(f"El producto {producto} no existe en el stock.")

    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ").lower()
        if producto in stock_productos:
            print(f"El producto {producto} ya existe en el stock.")
        else:
            try:
                unidades = int(input("Ingrese la cantidad inicial de unidades: "))
                if unidades >= 0:
                    stock_productos[producto] = unidades
                    print(f"Producto {producto} agregado con {unidades} unidades.")
                else:
                    print("La cantidad no puede ser negativa.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    elif opcion == '4':
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intente de nuevo.")
9#
agenda = {
    ('Lunes', '09:00'): "Reunión con equipo",
    ('Martes', '14:00'): "Clases de Python",
    ('Miércoles', '11:30'): "Consulta médica",
    ('Jueves', '16:00'): "Entrega de proyecto",
    ('Viernes', '10:00'): "Llamada con cliente"
}
dia_consulta = input("Ingrese el día que desea consultar (ejemplo: Lunes): ")
actividades_en_dia = [(hora, evento) for (dia, hora), evento in agenda.items() if dia.lower() == dia_consulta.lower()]
if actividades_en_dia:
    print(f"Actividades para el día {dia_consulta}:")
    for hora, evento in sorted(actividades_en_dia):
        print(f" - A las {hora}: {evento}")
else:
    print(f"No hay actividades registradas para el día {dia_consulta}.")
10#
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:")
print(capitales_paises)