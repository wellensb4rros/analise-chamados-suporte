import pandas as pd

# Ler o CSV
df = pd.read_csv('chamados.csv')

print("Dados:")
print(df)

print("\n---\n")

# Contagem por status
print("Chamados por status:")
print(df['status'].value_counts())

print("\n---\n")

# Contagem por prioridade
print("Chamados por prioridade:")
print(df['prioridade'].value_counts())