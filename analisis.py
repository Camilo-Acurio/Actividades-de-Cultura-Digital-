# Código para calcular el promedio de una lista de números
def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Datos de ejemplo (pueden ser notas o ventas)
mis_datos = [85, 90, 78, 92, 88]

resultado = calcular_promedio(mis_datos)
print(f"El promedio de los datos es: {resultado}")
