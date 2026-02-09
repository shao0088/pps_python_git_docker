from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)


@app.route("/")
def home():
    return "Hola, mundo"


@app.route("/frotar/<int:n_frases>")
def frotar_endpoint(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
