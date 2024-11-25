# define la lista de numeros
def max_in_list(numbers):
    if not numbers:
        raise ValueError("la lista is empty.")
    return max(numbers)

# prueba en pantalla
lista_de_numeros = [3, 0, 7, 8, 8, 77, 788]
resultado = max_in_list(lista_de_numeros)
print("El número más grande en la lista es:", resultado)
