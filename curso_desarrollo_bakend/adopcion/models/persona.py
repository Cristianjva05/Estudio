# se crea clase de persona

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


class Adoptante(Persona):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.mascotas_adoptadas = []   # Lista vacía al inicio

    def adoptar(self, mascota):
        self.mascotas_adoptadas.append(mascota)
        return f"{self.nombre} ha adoptado a {mascota.nombre}."
