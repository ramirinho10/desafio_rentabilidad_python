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
u_anterior = float(input("Ingrese las utilidades del año anterior, Deben ser distinto a 0!!!: "))

utilidades = p * u - gt
razon_de_utilidad = utilidades/u_anterior

print(f"Las utilidades obtenidades de este año es de: {utilidades}")
print(f"La razón entre las utilidades actuales y las del año pasado es de : {razon_de_utilidad:.2f}")