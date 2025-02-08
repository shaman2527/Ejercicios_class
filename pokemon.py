class Pokemon:

    def __init__(self, nombre, nivel, salud, color):
        self.nombre = nombre
        self.__nivel = None
        self.__salud = None
        self.color = color

        self.salud = salud
        self.nivel = nivel


        # Propiedades Leer y Modificar un atributo de la class privado y publico.

    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, salud):
        if salud > 0 and salud <= 100:
            self.__salud = salud
        else:
            print("LA salud no puede ser negativa",
                  "La salud no puder ser Mayor a 100")

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        if nivel > 0 and nivel <= 1000:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser negativo",
                  "El nivel no puede ser mayor a 1000")

