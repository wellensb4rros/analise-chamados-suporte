import sqlite3

conn = sqlite3.connect('chamados.db')
cursor = conn.cursor()

dados = [
    (1, "Erro no sistema", "aberto", "alta"),
    (2, "Lentidão", "fechado", "media"),
    (3, "Falha login", "aberto", "alta")
]

cursor.executemany("""
INSERT INTO chamados (id, titulo, status, prioridade)
VALUES (?, ?, ?, ?)
""", dados)

conn.commit()
conn.close()

print("Dados inseridos!")