
#Casas
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#IMPORTANTE: La expresion "+=" en Python es "suma y asigna" para guardar el valor en memoria

respuesta1_usuario = int(input("Pregunta 1. ¿Qué te gusta más, el amanecer o el anochecer?: 1) Amanecer o 2)Anochecer"))

if respuesta1_usuario == 1:
  Gryffindor +=1
  Ravenclaw +=1
elif respuesta1_usuario == 2:
  Hufflepuff +=1
  Slytherin +=1
else:
  print("respuesta incorrecta")

respuesta2_usuario = int(input("Pregunta 2. Cuando muera, quiero que la gente me recuerde como: 1) El Bueno, 2) El Grande, 3) El Sabio, 4) El Valiente "))

if respuesta2_usuario == 1:
  Slytherin +=4
elif respuesta2_usuario == 2:
  Hufflepuff +=4
elif respuesta2_usuario == 3:
  Ravenclaw +=4
elif respuesta2_usuario == 4:
  Gryffindor +=4
else:
  print("Entrada incorrecta")

print(f"Calificaciones casas: Gryffindor: {Gryffindor}. Ravenclaw: {Ravenclaw}. Hufflepuff: {Hufflepuff}. Slytherin: {Slytherin}")

if Gryffindor >= 4:
  print("El ganador es Gryffindor")
elif Ravenclaw >=4:
  print("El ganador es Ravenclaw")
elif Hufflepuff >=4:
  print("El ganador es Hufflepuff")
elif Slytherin >= 4:
  print("El ganador es Slitherin")
else:
  print("Nadie ganó")