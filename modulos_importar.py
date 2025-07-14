# Write code below 💖

from math import pi
from random import choice as ch

planets = ["Mercurio", "Venus", "Tierra", "Marte", "Saturno"]

random_planet = ch(planets)


def calcula_area(random_planet):
  r = 0

  if random_planet == "Mercurio":
    r += 2440
    planet_area = 4 * pi * r * r
    return print(f'Area of {random_planet}: {planet_area} sq mi')
  elif random_planet =='Venus':
    r += 6025
    planet_area = 4 * pi * r * r
    return print(f'Area of {random_planet}: {planet_area} sq mi')
  elif random_planet == 'Tierra':
    r += 6371
    planet_area = 4 * pi * r * r
    return print(f'Area of {random_planet}: {planet_area} sq mi')
  elif random_planet == 'Marte':
    r += 3390
    planet_area = 4 * pi * r * r
    return print(f'Area of {random_planet}: {planet_area} sq mi')
  elif random_planet == 'Saturno':
    r += 28232
    planet_area = 4 * pi * r * r
    return print(f'Area of {random_planet}: {planet_area} sq mi')
  else:
    print('Ups, ocurrio un error')

print(calcula_area(random_planet))
