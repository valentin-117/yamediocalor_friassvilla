# Solicitar el año, mes y día actuales
año_actual = int(input("Ingrese el año en curso: "))
mes_actual = int(input("Ingrese el mes en curso (1-12): "))
día_actual = int(input("Ingrese el día en curso (1-31): "))

# Pedir información de tres personas y calcular sus edades
for i in range(1, 4):
    nombre = input(f"\nIngrese el nombre de la persona {i}: ")
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    mes_nacimiento = int(input(f"Ingrese el mes de nacimiento de {nombre} (1-12): "))
    día_nacimiento = int(input(f"Ingrese el día de nacimiento de {nombre} (1-31): "))

    # Calcular la edad base
    edad = año_actual - año_nacimiento

    # Ajustar la edad si la persona aún no ha cumplido años este año
    if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and día_actual < día_nacimiento):
        edad -= 1

    print(f"{nombre} cumplirá {edad} años este año.")
