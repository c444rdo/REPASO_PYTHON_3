print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Programa que cuenta cuántas letras mayúsculas tiene una cadena introducida por el usuario
cadena = input("Ingresa una cadena: ")  # Solicitamos al usuario que ingrese una cadena
contador = 0  # Inicializamos un contador para las mayúsculas

# Iteramos sobre cada carácter de la cadena
for char in cadena:
    if char.isupper():  # Comprobamos si el carácter es una letra mayúscula
        contador += 1  # Si es mayúscula, incrementamos el contador

print(f"La cantidad de letras mayúsculas es: {contador}")  # Mostramos el resultado