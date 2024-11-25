def mas_larga(lista_palabras):
    if not lista_palabras:
        raise ValueError("La lista está vacía.")
    
    palabra_mas_larga = lista_palabras[0]
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

# prueba en pantalla. 
lista_de_palabras = ["lomas", "obo", "esternocleidomastoideo", "pepino", "crotolsmo"]
resultado = mas_larga(lista_de_palabras)
print("La palabra más larga es:", resultado)
