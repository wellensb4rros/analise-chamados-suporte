import sqlite3

conn = sqlite3.connect('chamados.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    status TEXT,
    prioridade TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")