# Solicitar al usuario las longitudes de los tres lados del triángulo
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Verificar el tipo de triángulo
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Las longitudes de los lados deben ser positivas.")
elif lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")