class Pokedex:
    def __init__(self, name, type, level, abilities, catched):
        self.name = name
        self.type = type
        self.level = level
        self.abilities = abilities
        self.catched = catched

    def mostrar_info(self):
        return f'Nombre: {self.name}, Tipo: {self.type}, Nivel: {self.level}, Habilidades: {self.abilities}, Capturado: {self.catched}'

picachu = Pokedex('Pikachu', 'Eléctrico', 25, ['Impactrueno', 'Ataque rápido'], True)

print(picachu.mostrar_info())