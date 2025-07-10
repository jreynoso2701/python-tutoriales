import random #Importar random

valor = random.randint(0,1) #Segun simula el lanzamiento de una moneda

if valor > 0.5:
  print("cara")
else: #Trucha, es importante poner bien el acomodo de la funcion
  print("sello")

