# Solicitar al usuario los dos números y la operación
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Verificar la operación y realizar el cálculo
if operation == "+":
    result = firstNumber + secondNumber
    print(f"The result of {firstNumber} + {secondNumber} is {result}")
elif operation == "-":
    result = firstNumber - secondNumber
    print(f"The result of {firstNumber} - {secondNumber} is {result}")
elif operation == "*":
    result = firstNumber * secondNumber
    print(f"The result of {firstNumber} * {secondNumber} is {result}")
elif operation == "/":
    if secondNumber != 0:
        result = firstNumber / secondNumber
        print(f"The result of {firstNumber} / {secondNumber} is {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Use +, -, *, or /.")
