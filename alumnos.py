alumnos = [
    ("Juan", 20, 85.5),
    ("María", 22, 90.0),
    ("Pedro", 21, 88.3),
    ("Ana", 19, 91.7)
]
mejor_alumno = max(alumnos, key=lambda x: x[2])

print("El alumno con el promedio más alto es:", mejor_alumno[0])
print("Edad:", mejor_alumno[1])
print("Promedio de calificaciones:", mejor_alumno[2])
