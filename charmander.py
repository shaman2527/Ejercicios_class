from asyncio import __main__

from tipofuego import TipoFuego

class Charmander(TipoFuego):

    def __init__(self, nombre: object, nivel: object, salud: object, color: object, temperatura_max: object):
        super().__init__(nombre, nivel, salud, color,temperatura_max)

if '__main__' == __main__:
    charmander_1 = Charmander('RBS', 100, 100, 'Rojo',10)

    print(charmander_1.temperatura_max)
    print(charmander_1.atacar())