print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Función que determina si un año es bisiesto
def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

# Ejemplo de uso:
año = int(input("Ingresa un año: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")