import pandas as pd

# Dado el siguiente DataFrame que contiene información de estudiantes y sus calificaciones:

data = {
    "Nombre": ["Ana", "Luis", "Pedro", "Sofía", "Lucía"],
    "Edad": [20, 22, 19, 21, 20],
    "Calificación": [85, 90, 78, 92, 88],
}
df = pd.DataFrame(data)

# Escribe una función llamada promedio_mayores_20 que calcule
# el promedio de las calificaciones de los estudiantes mayores de 20 años