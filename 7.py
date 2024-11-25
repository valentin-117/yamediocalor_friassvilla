# Pedir al usuario que ingrese 10 edades
edades = tuple(int(input(f"Ingrese la edad de la persona {i + 1}: ")) for i in range(10))

# Contar cuántas edades son mayores a 20
mayores_20 = sum(1 for edad in edades if edad > 20)

# Imprimir el resultado
print(f"La cantidad de personas con edades mayores a 20 es: {mayores_20}")
