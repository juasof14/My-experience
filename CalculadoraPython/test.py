def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: Tu eres bobo la verdad"
    return a / b

def calculadora():
    print("=== Calculadora By Juan David ===")
    print("Operaciones disponibles: +, -, *, /")
    while True:
        operacion = input("Ingrese la operacion (+, -, *, /) o 'Backspace' para abandonar: ")
        if operacion.lower() == 'backspace':
            print("Adios papu :D.")
            break

        if operacion not in ['+', '-', '*', '/']:
            print("Operacion no valida, mejor llamo a un profesor pa ti.")
            continue
        
        try:
            num1 = float(input("Ingrese el primer numero papu:"))
            num2 = float(input("Ingresa el segundo numero papu:"))
            if operacion == '+':
                resultado = sumar(num1, num2)
            elif operacion == '-':
                resultado = restar(num1, num2)
            elif operacion == '*':
                resultado = multiplicar(num1, num2)
            elif operacion == '/':
                resultado = dividir(num1, num2)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Entrada no valida, mejor llamo a un profesor pa ti.")
            continue
if __name__ == "__main__":
    calculadora()
    input("Escribe backspace pa salir")