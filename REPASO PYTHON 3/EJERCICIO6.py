print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Programa que calcula cuántos años cumplirán tres personas durante el año en curso

# Pedimos el año actual
anio_actual = int(input("Ingresa el año en curso: "))

# Pedimos el nombre y el año de nacimiento de tres personas
personas = []
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    anio_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    personas.append((nombre, anio_nacimiento))

# Calculamos los años que cumplirán durante el año en curso
for persona in personas:
    edad = anio_actual - persona[1]
    print(f"{persona[0]} cumplirá {edad} años en {anio_actual}.")