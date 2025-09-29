from models.mascota import Mascota
from models.persona import Adoptante
from models.refugio import Refugio

# Crear refugio y adoptante 
refugio = Refugio()
adoptante1 = Adoptante("Cristian Jose Vergara Alfoso", 24)

# Registrar mascotas iniciales
refugio.registrar_mascota(Mascota("Vicky", "Perra", 6))
refugio.registrar_mascota(Mascota("Lupita", "Gato", 2))
refugio.registrar_mascota(Mascota("Ducke", "Perro", 5))

# Menú interactivo
while True:
    print("======Menú Refugio de Mascotas======")
    print("1. Listar mascotas disponibles")
    print("2. Adoptar una mascota")
    print("3. Ver mascotas adoptadas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        disponibles = refugio.listar_disponibles()
        if disponibles:
            print("======ascotas disponibles:======")
            for m in disponibles:
                print(m)
        else:
            print("======No hay mascotas disponibles en este momento.======")

    elif opcion == "2":
        nombre_mascota = input("Ingresa el nombre de la mascota que quieres adoptar: ")
        print(refugio.asignar_adopcion(nombre_mascota, adoptante1))

    elif opcion == "3":
        if adoptante1.mascotas_adoptadas:
            print(f"======Mascotas adoptadas por {adoptante1.nombre}:")
            for m in adoptante1.mascotas_adoptadas:
                print(m)
        else:
            print("Aún no has adoptado ninguna mascota.")

    elif opcion == "4":
        print("¡Gracias por visitar el refugio!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
