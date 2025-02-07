class Pokemon:
    __tipo = 'Electrico'

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.__nivel = nivel
        self.__salud = salud
        self.__voltaje_max = voltaje_max
        self.__amperaje_max = amperaje_max
        self.color = color

    def atacar(self):
        print(f"Pikachu ataca y genera {self.__nivel / 4} de daño ")


pokemon = Pokemon('Simba', 750, 100, 6, 2, 'Rojo')
print(
    f"El pokemon llamado {pokemon.nombre}"
    f" tiene un nivel {pokemon.nivel}"
    f" y es de tipo {pokemon.tipo}"
    f" su voltaje es {pokemon._voltaje_max}")




