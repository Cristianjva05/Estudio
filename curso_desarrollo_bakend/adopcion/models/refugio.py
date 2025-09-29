from models.helpers import buscar_mascota

class Refugio:
    def __init__(self):
        self.__mascotas = []   # Lista privada de mascotas

    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_disponibles(self):
        return [m for m in self.__mascotas if not m.adoptado]

    def asignar_adopcion(self, nombre_mascota, adoptante):
        mascota = buscar_mascota(nombre_mascota, self.__mascotas)

        if mascota is None:
            return f" La mascota '{nombre_mascota}' no existe en el refugio."
        
        if mascota.adoptado:
            return f" La mascota '{mascota.nombre}' ya fue adoptada."
        
        # Si está disponible → marcar adoptada y asignar al adoptante
        mascota.adoptado = True
        adoptante.adoptar(mascota)
        return f" {adoptante.nombre} adoptó a {mascota.nombre}."
