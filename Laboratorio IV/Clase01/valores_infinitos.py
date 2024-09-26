import math
from decimal import Decimal

# manejo de valores infinitos
infinito_positivo = float('inf') #Esta cadena 'inf' representa el valor del infinito positivo, sino dice float NO funciona
print(f'Infinito positivo: {infinito_positivo}') #En la linea anterior definimos un infinito positivo y en esta linea lo confirma

#Comprobacion para ver si es realmente infinito
print(f'Es infinito?: {math.isinf(infinito_positivo)}') # Devuelve un booleano TRUE

# Infinito negativo
infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Modulo math - positivo
infinito_positivo = math.inf # Se asigna usando el modulo math
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

# Modulo math - negativo
infinito_positivo = -math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

# Modulo decimal
infinito_positivo = Decimal('Infinity') #Usamos una cadena llamada infinity
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')