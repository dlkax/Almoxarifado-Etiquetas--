from flask import Flask, render_template, request
import sqlite3
from datetime import date

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/", methods=["GET", "POST"])
def index():
    etiqueta = None
    erro = None

    if request.method == "POST":
        codigo = request.form.get("codigo")
        quantidade = request.form.get("quantidade")
        op = request.form.get("op")

        if not codigo or not quantidade or not op:
            erro = "Preencha todos os campos."
        else:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT descricao FROM produtos WHERE codigo = ?",
                (codigo,)
            )
            resultado = cursor.fetchone()
            conn.close()

            if resultado:
                etiqueta = {
                    "codigo": codigo,
                    "descricao": resultado[0],
                    "quantidade": quantidade,
                    "op": op,
                    "data": date.today().strftime("%d/%m/%Y")
                }
            else:
                erro = "Produto não encontrado."

    return render_template("index.html", etiqueta=etiqueta, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
