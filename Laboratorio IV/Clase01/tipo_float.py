# Profundizando en el tipo float
a = 3.0
print(f'a: {a:.2f}') # escribiendo :.2f le indico la cantidad de decimales que quiero que tenga(3.00)

# Constructor de tipo float -> puede recibir int y str
a = float(10) #Le pasamos un tipo entero (int)
print(f'a: {a:.2f}')
a = float('10') # recibe un string y lo convierte en float
print(f'a: {a:.2f}')

# Notacion exponencial (esto es para valores positivos o negativos)
a = 3e5 # Al numero 3 se le agregan (e) 5 ceros
print(f'a : {a}')

# La notacion exponencial permite simplificar los ceros(si queremos ver menos numeros)
# a = 3e50
# print(f'a : {a}')

# Le agregamos solos 2 ceros al final
a = 3e5
print(f'a : {a:.2f}')

# Valores negativos (simplificado)
a = 3e-5
print(f'a : {a}')

# Valores negativos (viendo todos los ceros)
a = 3e-5
print(f'a : {a:.5f}')

# Cualquier calculo que incluye un float, todo cambia a float

a = 4.0 + 5
print(a)
print(type(a))

