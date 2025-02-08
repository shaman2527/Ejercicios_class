from pokemon import Pokemon


class TipoElectrico(Pokemon):
    __tipo = 'Electric'

    def __init__(self, nombre: object, nivel: object, salud: object, voltaje_max: object, amperaje_max: object,
                 color: object) -> None:
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color)
        self.__voltaje_max = None
        self.__amperaje_max = None

        self.voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max

    # Propiedades de picachu

    @property
    def voltaje_max(self):
        return self.__voltaje_max

    @voltaje_max.setter
    def voltaje_max(self, voltaje_max):
        if 0 < voltaje_max <= 1000:
            self.__voltaje_max = voltaje_max
        else:
            print("No puede ser menor a 0",
                  "Ni mayor a 1000", "Voltaje")

    @property
    def amperaje_max(self):
        return self.__amperaje_max

    @amperaje_max.setter
    def amperaje_max(self, amperaje_max):
        if 0 < amperaje_max <= 500:
            self.__amperaje_max = amperaje_max
        else:
            print("El Amperímetro no puede ser menor a 100 ni mayor a 500")

    def atacar(self):
        print(f"Ataca con electricidad has suficiente daño {self.voltaje_max + self.amperaje_max / 4} de daño ")
