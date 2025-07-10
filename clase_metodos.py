class CuentaBancaria:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar_info(self):
        return f'Titular: {self.titular}, Cantidad: {self.cantidad}'
    
    def depositar(self, cantidad):
        self.cantidad += cantidad
        return f'Depositados {cantidad}. Nuevo saldo: {self.cantidad}'

    def retirar(self, cantidad):
        if cantidad > self.cantidad:
            return f'Fondos insuficientes. Saldo actual: {self.cantidad}'
        self.cantidad -= cantidad
        return f'Retirados {cantidad}. Nuevo saldo: {self.cantidad}'
    
# Ejemplo de uso
cuenta = CuentaBancaria('Juan Perez', 1000)
print(cuenta.mostrar_info())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.mostrar_info())

