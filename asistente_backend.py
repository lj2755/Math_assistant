import sympy
from sympy import symbols, Eq, solve, diff, integrate, simplify, factor, sympify

def resolver_ecuacion(ecuacion_str, variable_str):
    try:
        izquierda, derecha = ecuacion_str.split("=")
    except ValueError:
        return "Error: formato 'expresion = expresion' requerido."
    
    expr_izq = sympify(izquierda.strip())
    expr_der = sympify(derecha.strip())
    var = symbols(variable_str)
    ecuacion_simp = Eq(expr_izq, expr_der)

    try:
        soluciones = solve(ecuacion_simp, var)
        return f"Solución(es): {soluciones}"
    except Exception as e:
        return f"Error: {e}"


def calcular_derivada(funcion_str, variable_str):
    try:
        funcion = sympify(funcion_str)
        var = symbols(variable_str)
        derivada = diff(funcion, var)
        return f"Derivada: {derivada}"
    except Exception as e:
        return f"Error: {e}"


def calcular_integral(funcion_str, variable_str):
    try:
        funcion = sympify(funcion_str)
        var = symbols(variable_str)
        integral_resultado = integrate(funcion, var)
        return f"Integral: {integral_resultado} + C"
    except Exception as e:
        return f"Error: {e}"


def simplificar_expresion(expr_str):
    try:
        expr = sympify(expr_str)
        return f"Simplificado: {simplify(expr)}"
    except Exception as e:
        return f"Error: {e}"


def factorizar_expresion(expr_str):
    try:
        expr = sympify(expr_str)
        return f"Factorizado: {factor(expr)}"
    except Exception as e:
        return f"Error: {e}"
