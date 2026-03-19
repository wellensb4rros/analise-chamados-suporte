import sqlite3
import pandas as pd

# Conectar ao banco
conn = sqlite3.connect('chamados.db')

# Fazer consulta SQL e jogar no pandas
df = pd.read_sql_query("SELECT * FROM chamados", conn)

# Mostrar os dados
print("Dados vindos do banco:")
print(df)

# Fechar conexão
conn.close()