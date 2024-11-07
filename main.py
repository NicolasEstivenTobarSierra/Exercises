# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es par o impar utilizando el operador módulo (%)
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")