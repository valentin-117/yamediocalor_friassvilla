def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4, pero no por 100, a menos que sea divisible por 400
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Solicitar al usuario que ingrese un año
año = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto y mostrar el resultado
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
