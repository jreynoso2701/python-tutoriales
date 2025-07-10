import random
import math

simbolos = ['🍒', ' 🍇', '🍉', '7️⃣']



def play_tragamonedas(decision):
    while decision.lower() == "si":
        resultados = random.choices(simbolos, k=3)
        print("Resultados:", resultados)
        
        if resultados[0] == resultados[1] == resultados[2]:
            print("¡Ganaste!")
        elif resultados[0] == '7️⃣' and resultados[1] == '7️⃣' and resultados[2] == '7️⃣':
            print("¡Ganaste el premio mayor!")
        else:
            print("Inténtalo de nuevo.")
        
        decision = input("¿Quieres jugar de nuevo? (Si/No): ")



print("Bienvenido a la máquina tragamonedas")
decision = input("¿Quieres jugar? (Si/No): ")
if decision.lower() == "si":
    play_tragamonedas(decision)