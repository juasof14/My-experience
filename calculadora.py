def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    print("=== Calculadora Simple ===")
    print("Operaciones disponibles: +, -, *, /")

    while True:
        operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para terminar: ")
        if operacion.lower() == 'salir':
            print("Saliendo de la calculadora.")
            break
        if operacion not in ['+', '-', '*', '/']:
            print("Operación no válida. Intente de nuevo.")
            continue
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor ingrese números.")
            continue

        if operacion == '+':
            resultado = sumar(num1, num2)
        elif operacion == '-':
            resultado = restar(num1, num2)
        elif operacion == '*':
            resultado = multiplicar(num1, num2)
        elif operacion == '/':
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()
    input("Presiona Enter para salir")