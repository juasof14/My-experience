import ast

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b
def potencia(a, b):
    return a ** b

class SafeEval(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        return super().visit(node)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.op
        if isinstance(op, ast.Add):
            return left + right
        if isinstance(op, ast.Sub):
            return left - right
        if isinstance(op, ast.Mult):
            return left * right
        if isinstance(op, ast.Div):
            return left / right
        if isinstance(op, ast.Pow):
            return left ** right
        if isinstance(op, ast.Mod):
            return left % right
        raise ValueError(f"Operador no permitido: {op}")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError("Operador unario no permitido")

    def visit_Num(self, node):  # For Python <3.8
        return node.n

    def visit_Constant(self, node):  # For Python >=3.8
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Solo se permiten números")

    def generic_visit(self, node):
        raise ValueError(f"Nodo no permitido en la expresión: {type(node).__name__}")

def eval_expr(expr):
    expr = expr.replace('^', '**')  # allow using ^ as power like users might expect
    node = ast.parse(expr, mode='eval')
    evaluator = SafeEval()
    return evaluator.visit(node)

def calculadora():
    print("=== Calculadora 2 ===")
    while True:
        expresion = input("Ingrese una operación (o 'salir' para terminar): ").strip()
        if expresion.lower() == 'salir':
            print("Saliendo de la calculadora.")
            break
        if not expresion:
            continue
        try:
            resultado = eval_expr(expresion)
        except ZeroDivisionError:
            print("Error: División por cero")
            continue
        except Exception as e:
            print(f"Error en la expresión: {e}")
            continue

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()



