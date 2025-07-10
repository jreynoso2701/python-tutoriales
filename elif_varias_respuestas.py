import random

pregunta = input("Cual es tu pregunta?")
print("Tu pregunta:"+pregunta)

num_random = random.randint(1,9)

if num_random == 1:
 respuesta = "Si, definitivamente"
elif num_random == 2:
 respuesta = "Es complicado"
elif num_random == 3:
 respuesta = "Sin duda"
elif num_random == 4:
 respuesta = "Mejor haz otra pregunta"
elif num_random == 5:
 respuesta = "Pregunta más tarde"
elif num_random == 6:
 respuesta = "Mejor no te digo"
elif num_random == 7:
 respuesta = "Mi fuente dice que no"
elif num_random == 8:
 respuesta = "No es algo bueno"
elif num_random == 9:
 respuesta = "Muy dudoso"
else:
 respuesta = "Ya no hay respuestas"
#checa la indentacion

print("Respuesta IA: " + respuesta)