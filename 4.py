def contar_mayusculas(cadena):
    if not cadena:
        return 0  # Si la cadena está vacía, retorna 0
    
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador

# Programa principal
cadena = input("Por favor, ingrese una cadena: ")
cantidad_mayusculas = contar_mayusculas(cadena)
print(f"La cadena tiene {cantidad_mayusculas} letras mayúsculas.")
