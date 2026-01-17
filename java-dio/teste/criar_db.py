import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    codigo TEXT PRIMARY KEY,
    descricao TEXT NOT NULL
)
""")

# Inserir produtos
cursor.execute("""
INSERT OR IGNORE INTO produtos (codigo, descricao) VALUES
("1-0012922", "GAXETA ZERO 6"),
("4-2752/002", "GRADE ZERO 8"),
("8-6131/900CM", "CONJUNTO MOVEL"),
("4-4136/122", "TWEETER REVO 6"),
("1-0203002", "TWEETER DOME TITANIUM IMPORTADO"),
("1-6102003", "TWEETER DOME"),
("8-6009/160", "PINO C/ CENTRAGEM + TWEETER BULLET")
""")

conn.commit()
conn.close()

print("database criado")
