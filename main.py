# Solicitar al usuario que ingrese la calificación
calification = float(input("Ingresa tu calificación: "))

# Verificar si la calificación es aprobatoria o reprobatoria
if calification >= 60:
    print("Aprobado")
else:
    print("Reprobado")