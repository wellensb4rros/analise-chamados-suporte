import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Análise de Chamados")

conn = sqlite3.connect('chamados.db')

df = pd.read_sql_query("SELECT * FROM chamados", conn)

st.write("### Dados:")
st.dataframe(df)

st.write("### Chamados por status")
st.write(df['status'].value_counts())

st.write("### Chamados por prioridade")
st.write(df['prioridade'].value_counts())

conn.close()
