from flask import Flask, request, jsonify, render_template
from asistente_backend import (
    resolver_ecuacion,
    calcular_derivada,
    calcular_integral,
    simplificar_expresion,
    factorizar_expresion
)
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Renderizamos la página HTML principal (index.html)
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    # Recibimos los datos enviados desde el frontend (p.ej. por AJAX o fetch)
    data = request.get_json()
    operacion = data.get("operacion")
    expresion = data.get("expresion", "")
    variable = data.get("variable", "x")  # por defecto x

    resultado = "Operación no reconocida."

    if operacion == "resolver_ecuacion":
        resultado = resolver_ecuacion(expresion, variable)
    elif operacion == "derivada":
        resultado = calcular_derivada(expresion, variable)
    elif operacion == "integral":
        resultado = calcular_integral(expresion, variable)
    elif operacion == "simplificar":
        resultado = simplificar_expresion(expresion)
    elif operacion == "factorizar":
        resultado = factorizar_expresion(expresion)

    # Devolvemos el resultado como JSON
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    # Ejecutar la app en modo desarrollo en http://localhost:5000
    app.run(debug=True, port=os.getenv("PORT", 5000))   