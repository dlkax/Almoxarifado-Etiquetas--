from flask import Flask, render_template, request
import sqlite3
from datetime import date
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():
    return sqlite3.connect(DB_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    etiquetas = [None, None, None, None]
    erro = None

    if request.method == "POST":
        conn = get_db()
        cursor = conn.cursor()

        def buscar(codigo, quantidade, op):
            cursor.execute(
                "SELECT descricao FROM produtos WHERE codigo = ?",
                (codigo,)
            )
            resultado = cursor.fetchone()
            if resultado:
                return {
                    "codigo": codigo,
                    "descricao": resultado[0],
                    "quantidade": quantidade,
                    "op": op,
                    "data": date.today().strftime("%d/%m/%Y")
                }
            return None

        for i in range(4):
            cod = request.form.get(f"codigo{i+1}")
            qtd = request.form.get(f"quantidade{i+1}")
            op = request.form.get(f"op{i+1}")

            if cod and qtd and op:
                etiqueta = buscar(cod, qtd, op)
                if etiqueta:
                    etiquetas[i] = etiqueta
                else:
                    erro = f"Produto da etiqueta {i+1} não encontrado."

        conn.close()

    return render_template(
        "index.html",
        etiqueta1=etiquetas[0],
        etiqueta2=etiquetas[1],
        etiqueta3=etiquetas[2],
        etiqueta4=etiquetas[3],
        erro=erro
    )

if __name__ == "__main__":
    app.run(debug=True)