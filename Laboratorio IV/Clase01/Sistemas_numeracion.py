# Profundizando en los sistemas de numeracion

# Sistema Decimal
a = 10
print(f"a decimal: {a}")

# Sistema binario
a= 0b1010
print(f"a binario: {a}")

# Sistema octal
a = 0o12
print(f"a octal: {a}")

# Sistema hexadecimal
a = 0xA
print(f"a hexadecimal: {a}")

# Utilizamos constructor de tipo int para convertir
# Base Decimal
a = int('23', 10) #El 10 es la base
print(f"a base decimal: {a}")

# Base binaria
a = int('10111', 2) # El 2 indica que es binario
print(f"a base binario: {a}")

# Base octal
a = int('27', 8) # La base es 8, indica que tenemos un valor numerico del sistema octal
print(f"a base octal: {a}")

# Base hexadecimal
a = int('17', 16) # El 16 indica que es hexadecimal
print(f"a base hexadecimal: {a}")

# Base 5 sus valores son de 0 a 4
a = int('34', 5)
print(f"a base 5: {a}")