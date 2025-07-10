#Un while bucle es muy similar a una ifsentencia. Al igual que una ifsentencia, ejecuta el código si la condición es True.

#Sin embargo, la diferencia es que el whilebucle continuará ejecutando el código dentro de él, una y otra vez, mientras la condición sea True.

print("Bienvenido al cajero automático")

pin = int(input("Ingrese su PIN: "))

while pin != 1234:
    pin = int(input("PIN Incorrecto. Ingrese su PIN nuevamente: "))
if pin == 1234:
    print("PIN correcto. Acceso concedido.")
