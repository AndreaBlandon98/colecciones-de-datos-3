meses = [
    ("Enero", 31),
    ("Febrero", 28),
    ("Marzo", 31),
    ("Abril", 30),
    ("Mayo", 31),
    ("Junio", 30),
    ("Julio", 31),
    ("Agosto", 31),
    ("Septiembre", 30),
    ("Octubre", 31),
    ("Noviembre", 30),
    ("Diciembre", 31)
]
numero_mes = int(input("Ingrese el número de mes (1-12): "))
if numero_mes < 1 or numero_mes > 12:
    print("Número de mes inválido.")
else:
    nombre_mes, dias = meses[numero_mes - 1]
    print(f"El mes de {nombre_mes} tiene {dias} días.")
