"""
Utilidades = P * U - GT
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
"""

print("Ingrese los datos solicitados")
p = float(input("Ingrese el precio de suscripción: "))
u = int(input("Ingrese el numero de usuarios: "))
gt = float(input("Ingrese gasto total: "))

utilidades = p * u - gt

print(f"Las utilidades obtenidades son: {utilidades}")
