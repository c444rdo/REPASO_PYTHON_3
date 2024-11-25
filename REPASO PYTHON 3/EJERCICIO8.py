print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Definimos una lista de nombres
nombres = ['Ana', 'Pedro', 'Alberto', 'Luis', 'Carlos', 'Amanda']

# Pedimos al usuario que ingrese una letra para buscar
letra = input("Ingresa una letra para buscar: ").lower()  # Convertimos la letra a minúsculas para no diferenciar entre mayúsculas y minúsculas

# Contamos cuántos nombres comienzan con la letra proporcionada
contador = sum(1 for nombre in nombres if nombre[0].lower() == letra)

print(f"Hay {contador} nombres que comienzan con la letra {letra.upper()}.")