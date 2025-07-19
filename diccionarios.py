usuario_sistema = {
  'nombre': 'Juan',
  'ap_paterno': 'Reynoso',
  'edad': 36,
  'activo': True
}

#Accesando a elementos:
print('Nombre: ', usuario_sistema['nombre'])
print('Apellido: ', usuario_sistema['ap_paterno'])
print('Edad: ', usuario_sistema['edad'])
print('Activo: ', usuario_sistema['activo'])

#Modificando un dato:
usuario_sistema['edad'] = 37
print('Edad actualizada: ', usuario_sistema['edad'])

#Metodos de los diccionarios:
print('Keys: ', usuario_sistema.keys())
print('Values: ', usuario_sistema.values())
print('Items: ', usuario_sistema.items())