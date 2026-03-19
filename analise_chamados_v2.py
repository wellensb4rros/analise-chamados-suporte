import pandas as pd

def carregar_dados(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        print("✅ Dados carregados com sucesso!\n")
        return df
    except Exception as e:
        print("❌ Erro ao carregar arquivo:", e)
        return None


def analisar_status(df):
    print("📊 Chamados por status:")
    print(df['status'].value_counts())
    print("\n----------------------\n")


def analisar_prioridade(df):
    print("📊 Chamados por prioridade:")
    print(df['prioridade'].value_counts())
    print("\n----------------------\n")


def main():
    caminho = 'chamados.csv'
    
    df = carregar_dados(caminho)
    
    if df is not None:
        print("🔎 Visualização dos dados:")
        print(df.head())
        print("\n----------------------\n")
        
        analisar_status(df)
        analisar_prioridade(df)


if __name__ == "__main__":
    main()