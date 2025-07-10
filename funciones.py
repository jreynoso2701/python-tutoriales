# Write code below 💖

menu = ['🍔 Cheeseburger',
        '🍟 Fries',
        '🥤 Soda',
        '🍦 Ice Cream',
        '🍪 Cookie']

def get_item(i):
  if i == 1:
    resultado = menu[0]
    return resultado
  elif i == 2:
    resultado = menu[1]
    return print("elegiste:"+ resultado)
  elif i == 3:
    resultado = menu[2]
    return print("elegiste:"+ resultado)
  elif i == 4:
    resultado = menu[3]
    return print("elegiste:"+ resultado)
  elif i == 5:
    resultado = menu[4]
    return print("elegiste:"+ resultado)

def welcome():
  print("Bienvenido a FastFood, a continuación le presentamos nuestro menu: ")
  print(menu)
  
print(welcome())
opcion = int(input("Elija la opcion que desea ordenar: "))

print(get_item(opcion))