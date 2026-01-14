from flask import Flask, jsonify, request
from controllers.gastos_controller import GastosController

app = Flask(__name__)
controller = GastosController()

@app.route("/")
def home():
    return jsonify({"message": "API FinTrack Online!"})

@app.route("/gastos", methods=["POST"])
def cadastro_gasto():
    data = request.json
    response = controller.adicionar_gasto(data)
    return jsonify(response)

@app.route("/gastos", methods=["GET"])
def listar_gastos():
    response = controller.listar_gastos()
    return jsonify(response)

@app.route("/gastos/estatisticas", methods=["GET"])
def estatisticas():
    response = controller.estatisticas()
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)