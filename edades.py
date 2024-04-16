alumnos = {}

while True:
    nombre = input("Ingrese el nombre del alumno (o * para terminar): ")
    if nombre == '*':
        break
    edad = int(input("Ingrese la edad de {} : ".format(nombre)))
    alumnos[nombre] = edad
print("Estudiantes mayores de edad:")
for nombre, edad in alumnos.items():
    if edad >= 18:
        print(f"{nombre} - {edad} años")
alumno_mayor = max(alumnos, key=alumnos.get)
print(f"El alumno mayor es: {alumno_mayor} - {alumnos[alumno_mayor]} años")




