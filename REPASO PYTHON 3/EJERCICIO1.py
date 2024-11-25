print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Función que recibe una lista de números y devuelve el más grande
def max_in_list(numeros):
    # Comprobamos si la lista está vacía
    if not numeros:
        return None  # Si la lista está vacía, retornamos None
    max_num = numeros[0]  # Asumimos que el primer número es el mayor inicialmente
    # Iteramos sobre los demás números para encontrar el máximo
    for num in numeros:
        if num > max_num:
            max_num = num  # Actualizamos el máximo si encontramos un número mayor
    return max_num  # Devolvemos el número más grande

# Ejemplo de uso:
print(max_in_list([1, 3, 7, 2, 5]))  # Salida: 7