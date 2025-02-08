from asyncio import __main__

from tipoelectrico import TipoElectrico


class Pikachu(TipoElectrico):

    def __init__(self, nombre: object, nivel: object, salud: object, voltaje_max: object, amperaje_max: object,
                 color: object) -> None:
        super().__init__(nombre=nombre, nivel=nivel, salud=salud,
                         color=color, voltaje_max=voltaje_max,
                         amperaje_max=amperaje_max)

        self.color = color

if '__main__' == __main__:
    pokemon_pikachu = Pikachu('Simba', 100, 100, 50, 2, 'Rojo')

    pokemon_pikachu.atacar()
