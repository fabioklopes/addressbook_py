# streamlit_app.py
import streamlit as st
import requests
import pandas as pd

# URL da sua API Django (ajuste se estiver em produção)
API_URL = "http://127.0.0.1:8000/api/meusmodelos/"

st.title("Dashboard com Dados do Django")

# Função para buscar dados da API
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Lança um erro para respostas ruins (4xx ou 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao conectar com a API: {e}")
        return None

st.header("Visualizando Dados")

if st.button("Carregar Dados do Projeto Django"):
    data = fetch_data(API_URL)
    if data:
        st.success("Dados carregados com sucesso!")
        df = pd.DataFrame(data)
        st.dataframe(df)

        st.subheader("Gráfico de Exemplo")
        # Supondo que você tenha uma coluna 'valor' e 'categoria'
        if 'valor' in df.columns and 'categoria' in df.columns:
            chart_data = df.groupby('categoria')['valor'].sum()
            st.bar_chart(chart_data)
    else:
        st.warning("Não foi possível carregar os dados.")

# Exemplo de como enviar dados (POST)
st.header("Criar Novo Item")
with st.form("new_item_form"):
    nome = st.text_input("Nome do Item")
    valor = st.number_input("Valor", min_value=0)
    submitted = st.form_submit_button("Criar")

    if submitted:
        new_data = {'nome': nome, 'valor': valor}
        try:
            response = requests.post(API_URL, json=new_data)
            response.raise_for_status()
            st.success("Item criado com sucesso!")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao criar item: {e}")
            st.json(e.response.json()) # Mostra o erro retornado pela API do Django
