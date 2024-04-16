libreta_contactos = []
def agregar_contacto(nombre, telefono):
    nuevo_contacto = (nombre, telefono)
    libreta_contactos.append(nuevo_contacto)
    print("Contacto agregado:", nombre)
def buscar_contacto(nombre):
    for contacto in libreta_contactos:
        if contacto[0] == nombre:
            return contacto
    return None
def listar_contactos():
    if len(libreta_contactos) > 0:
        print("Lista de contactos:")
        for contacto in libreta_contactos:
            print(contacto[0], "-", contacto[1])
    else:
        print("La libreta de contactos está vacía.")
agregar_contacto("Andrea", "123456789")
agregar_contacto("Carlos", "987654321")
agregar_contacto("Luisa", "456789123")

print("\nBuscando contacto:")
contacto_buscado = buscar_contacto("Andrea")
if contacto_buscado:
    print("Contacto encontrado:", contacto_buscado[0], "-", contacto_buscado[1])
else:
    print("Contacto no encontrado.")

print("\nListando contactos:")
listar_contactos()
