import sqlite3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

conn = sqlite3.connect(BASE_DIR / "database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    codigo TEXT PRIMARY KEY,
    descricao TEXT NOT NULL
)
""")

with open(BASE_DIR / "dados_convertidos.txt", encoding="utf-8") as f:
    texto = f.read()

dados = [
    (codigo.strip(), descricao.strip())
    for codigo, descricao in re.findall(r'\("([^"]+)","([^"]+)"\)', texto)
]

cursor.executemany(
    "INSERT OR IGNORE INTO produtos (codigo, descricao) VALUES (?, ?)",
    dados
)

conn.commit()
conn.close()

print(f"{len(dados)} produtos carregados com sucesso.")
