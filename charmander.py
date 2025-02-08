from pokemon import Pokemon


class Charmander(Pokemon):

    def __init__(self, nombre: object, nivel: object, salud: object, color: object) -> None:
        super().__init__(nombre, nivel, salud, color)


charmander_1 = Charmander('RBS', 100, 100, 'Rojo')

print(charmander_1.salud)
print(charmander_1.nivel)
print(charmander_1.nombre)
print(charmander_1.color)
