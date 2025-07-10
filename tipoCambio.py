# Clase para transformar morralla de diferentes monedas a dolares

co = 0.00025
pe = 0.28
br = 0.18

morralla_co = int(input("Cuanta morralla tienes en Pesos Colombianos?:"))
morralla_pe = int(input("Cuanta morralla tienes en Soles Peruanos?:"))
morralla_br = int(input("Cuanta morralla tienes en Reales Brazileños?:"))

total_dolares = (morralla_co * co) + (morralla_pe * pe) + (morralla_br * br)
print(total_dolares)