from pokemon import Pokemon


class Pikachu(Pokemon):
    tipo = 'Electrico'

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color)
        self.__voltaje_max = None
        self.__amperaje_max = None
        self.color = color

        self.voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max


    #Propiedades de picachu

    @property
    def voltaje_max(self):
        return self.__voltaje_max

    @voltaje_max.setter
    def voltaje_max(self, voltaje_max):
        if voltaje_max > 0 and voltaje_max <= 1000:
            self.__voltaje_max = voltaje_max
        else:
            print("No puede ser menor a 0",
                  "Ni mayor a 1000","Voltaje")

    @property
    def amperaje_max(self):
        return self.__amperaje_max

    @amperaje_max.setter
    def amperaje_max(self, amperaje_max):
        if amperaje_max > 0 and amperaje_max <= 500:
            self.__amperaje_max = amperaje_max
        else:
            print("El Amperimetro no puede ser menor a 100 ni mayor a 500")

    def atacar(self):
        print(f"Pikachu ataca y genera {self.__nivel / 4} de daño ")


pokemon_pikachu = Pikachu('Simba', 1000, 100, 1020, 600, 'Rojo')

pokemon_pikachu.voltaje_max
pokemon_pikachu.amperaje_max