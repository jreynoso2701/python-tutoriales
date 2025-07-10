# El for es como un blucke que lista la instancia de un objeto iterable, en este caso un rango de números del 99 al 1.
# El range(99, 0, -1) genera una secuencia de números desde 99 hasta 1, decreciendo de uno en uno.
for cervezas in range(99, 0, -1):# (inicio, fin, paso)
    if cervezas == 1:
        print(f"{cervezas} cerveza en la nevera, {cervezas} cerveza.")
    else:
        print(f"{cervezas} cervezas en la nevera, {cervezas} cervezas.")
    if cervezas > 1:
        print(f"Queda(n) {cervezas - 1} {'cerveza' if cervezas - 1 == 1 else 'cervezas'} en la nevera.\n")
    else:
        print("No quedan más cervezas en la nevera.\n")