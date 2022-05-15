"""
Utilidades = P * U - GT
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
"""

print("Ingrese los datos solicitados")
p = float(input("Ingrese el precio de suscripción: "))
u_normal = int(input("Ingrese el numero de usuarios normales: "))
u_premium = int(input("Ingrese el numero de usuarios premium: "))
gt = float(input("Ingrese gasto total: "))

utilidades = p * u_normal + p * 1.5 * u_premium - gt

print(f"Las utilidades obtenidades son: {utilidades}")

