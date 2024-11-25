print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Función que recibe una lista de palabras y devuelve la palabra más larga
def mas_larga(palabras):
    # Comprobamos si la lista está vacía
    if not palabras:
        return None  # Si la lista está vacía, retornamos None
    palabra_max = palabras[0]  # Asumimos que la primera palabra es la más larga
    # Iteramos sobre las demás palabras
    for palabra in palabras:
        if len(palabra) > len(palabra_max):
            palabra_max = palabra  # Actualizamos la palabra más larga si encontramos una mayor
    return palabra_max  # Devolvemos la palabra más larga

# Ejemplo de uso:
print(mas_larga(['manzana', 'pera', 'sandía', 'plátano']))  # Salida: 'manzana'