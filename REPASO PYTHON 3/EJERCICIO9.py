print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Función que cuenta las vocales en una palabra
def contar_vocales(palabra):
    vocales = 'aeiou'  # Definimos las vocales
    conteo = {v: 0 for v in vocales}  # Creamos un diccionario para contar cada vocal
    # Iteramos sobre cada letra de la palabra
    for letra in palabra.lower():  # Convertimos la palabra a minúsculas para no diferenciar entre mayúsculas y minúsculas
        if letra in vocales:
            conteo[letra] += 1  # Incrementamos el contador de la vocal

    return conteo  # Devolvemos el diccionario con los conteos

# Ejemplo de uso:
palabra = input("Ingresa una palabra: ")
vocales_contadas = contar_vocales(palabra)
print("Conteo de vocales:", vocales_contadas)