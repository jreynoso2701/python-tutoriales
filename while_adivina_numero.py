numero = 0
intentos = 3

while numero != 5 and intentos > 0:
    numero = int(input("Adivina el número (entre 1 y 10): "))
    intentos -= 1
    if numero == 5:
        print("¡Correcto!")
    else:
        print(f"Incorrecto, te quedan {intentos} intentos.")

