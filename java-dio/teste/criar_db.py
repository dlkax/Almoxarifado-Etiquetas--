import sqlite3
import re

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    codigo TEXT PRIMARY KEY,
    descricao TEXT NOT NULL
)
""")

with open("dados_convertidos.txt", encoding="utf-8") as f:
    texto = f.read()

dados = re.findall(r'\("([^"]+)","([^"]+)"\)', texto)

cursor.executemany(
    "INSERT OR IGNORE INTO produtos (codigo, descricao) VALUES (?, ?)",
    dados
)

conn.commit()
conn.close()

print(f"{len(dados)} produtos carregados com sucesso.")
