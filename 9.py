def contar_vocales(palabra):
    # Inicializamos un diccionario para contar las vocales
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    # Recorremos cada letra de la palabra
    for letra in palabra.lower():  # Convertimos a minúsculas para que sea insensible a mayúsculas
        if letra in vocales:
            vocales[letra] += 1
    
    # Imprimir la cantidad de cada vocal
    for vocal, cantidad in vocales.items():
        print(f"La letra '{vocal}' aparece {cantidad} veces.")
    

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Llamar a la función contar_vocales para contar las vocales
contar_vocales(palabra)
