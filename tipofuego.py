from pokemon import Pokemon


class TipoFuego(Pokemon):
    __tipo = 'Fuego'

    def __init__(self, nombre, nivel, salud, color, temperatura_max):
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color)
        self.__temperatura_max = None

        self.temperatura_max = temperatura_max

    @property
    def temperatura_max(self):
        return self.__temperatura_max

    @temperatura_max.setter
    def temperatura_max(self, temperatura_max):
        if temperatura_max > 0:
            self.__temperatura_max = temperatura_max

        else:
            print("La temperatura no puede ser Negativa")

    def atacar(self):
        print(f"Ataca y genera Fuego {self.temperatura_max * 0.5} de daño ")
