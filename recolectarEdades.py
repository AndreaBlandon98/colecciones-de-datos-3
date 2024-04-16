num_edades = int(input("Ingrese la cantidad de edades a recolectar: "))
edades = []
for i in range(num_edades):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad)
edades_ordenadas = sorted(edades)

print("Edades recolectadas:", edades)
print("Edades ordenadas de menor a mayor:", edades_ordenadas)
