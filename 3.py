def filtrar_palabras(lista_palabras, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor de 'n' debe ser un entero no negativo.")
    if not lista_palabras:
        return []  # SI no hay nada en la lista, se regresa vacia.
    
    return [palabra for palabra in lista_palabras if len(palabra) > n]

# Prueba de la función
lista_de_palabras = ["sol", "mariposa", "computadora", "día", "extraordinario"]
n = 5
resultado = filtrar_palabras(lista_de_palabras, n)
print("Palabras con más de", n, "caracteres:", resultado)
