#creo la clase
class Mascota:

    def __init__(self, nombre: str, especie: str, edad: int, adoptado: bool = False):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado

    # crea como se mostrará la clase 
    def __str__(self):
        estado = "Adoptado" if self.adoptado else "No adoptado"
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años, Estado: {estado}"
