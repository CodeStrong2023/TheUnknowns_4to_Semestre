# Bool contiene los valores de true y false
#Los tipos numericos, es falso para el 0 (cero) y true para los demas valores

valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resulado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resulado: {resultado}')

# Tipo string -> False '' (representa una cadena vacia), True demas valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resulado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: {valor}, Resulado: {resultado}')

# Tipo de colecciones -> False para colecciones vacias
# Tipo de colecciones -> True para todas las demas
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, Resulado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'valor de una lista con elementos: {valor}, Resulado: {resultado}')

# Tupla -> False para corchetes vacios
# Tupla -> True para todas las demas
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia: {valor}, Resulado: {resultado}')

valor = (5,) #poniendole una coma la hace ser tupla
resultado = bool(valor)
print(f'valor de una tupla con elementos: {valor}, Resulado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, Resulado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido':'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario con elementos: {valor}, Resulado: {resultado}')

# Sentencias de control con bool
if '': #es falso porque esta vacia la cadena
    print('Regresa verdadero')
else:
    print('Regresa falso')

if 'Hola': #es verdadero porque hay una cadena
    print('Regresa verdadero')
else:
    print('Regresa falso')

if bool('Hola'): #es lo mismo poniendo el bool
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')
    