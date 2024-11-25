print ("Martínez Estrada Ricardo / NO. de control: 1193 / 25-11-2024")
print (" ")

# Definimos una tupla con 10 edades de personas
edades = (18, 25, 34, 16, 42, 19, 33, 28, 45, 21)

# Contamos cuántas personas tienen edades mayores a 20
mayores_a_20 = sum(1 for edad in edades if edad > 20)

print(f"Hay {mayores_a_20} personas con edades superiores a 20.")