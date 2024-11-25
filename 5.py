# Programa para convertir un número binario a entero
binario = input("Ingrese un número binario: ")

try:
    entero = int(binario, 2)
    print(f"El número binario {binario} convertido a entero es: {entero}")
except ValueError:
    print("Entrada no válida. Asegúrate de ingresar solo números binarios (0 y 1).")
