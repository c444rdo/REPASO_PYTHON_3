print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Función que recibe una lista de palabras y un número n,
# y devuelve las palabras que tengan más de n caracteres
def filtrar_palabras(palabras, n):
    # Usamos list comprehension para filtrar las palabras
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) > n]
    return palabras_filtradas  # Devolvemos la lista filtrada

# Ejemplo de uso:
print(filtrar_palabras(['manzana', 'pera', 'sandía', 'plátano'], 5))  # Salida: ['manzana', 'sandía', 'plátano']