import random

# Crea una función que tome como input una lista de números y retorne el número más grande.
# No está permitido usar la función predefinida max ni paquetes adicionales.

random.seed(42)
x = random.sample(range(1, 1010), 50)

# Comienza tu respuesta aca:
def numGrande
    numero=0
    for i in x:
        if i>1009:
            numero=i

    print(numero)

numGrande(x)

