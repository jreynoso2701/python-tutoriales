
# Con init puedes inicializar los atributos de una clase de forma más sencilla y ordenada.
# Al principio es meter mas codigo, pero al final es más fácil de leer y mantener a largo plazo.
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

zapopan = City('Zapopan', 'Jalisco', 100, ['Andares, Plaza Patria'])
tonala = City('Tonala', 'Jalisco', 80, ['Chedraui', 'Tianguis'])

print(vars(zapopan))
print(vars(tonala))

# Lo curioso es que las respuestas son estructuras tipo json.