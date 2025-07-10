#Un while bucle es muy similar a una ifsentencia. Al igual que una ifsentencia, ejecuta el código si la condición es True.

#Sin embargo, la diferencia es que el whilebucle continuará ejecutando el código dentro de él, una y otra vez, mientras la condición sea True.


cheque_mama_koala = str(input("Ya cayo el cheque de mama koala: (Si/No): "))

while cheque_mama_koala.lower() != "si":
    print("Aun no cayo el cheque de mama koala")
    cheque_mama_koala = str(input("Ya cayo el cheque de mama koala: (Si/No): "))

print("¡Hasta que!, a quemarlo de una vez")