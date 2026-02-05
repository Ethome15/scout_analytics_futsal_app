import pandas as pd
import streamlit as st

def ler_arquivo(upload):
    nome = upload.name.lower()

    try:
        if nome.endswith(".xlsx"):
            return pd.read_excel(upload)

        elif nome.endswith(".csv"):
            try:
                return pd.read_csv(upload)
            except:
                return pd.read_csv(upload, sep=";")

        else:
            st.error("Formato não suportado")
            return None

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None