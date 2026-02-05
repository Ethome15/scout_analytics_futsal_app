import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from services.data_analytics import media, media_individual

#AQUI VAI FICAR OS GRAFICOS
media()
def grafico_media_geral():
    medias = media()

    fig, ax = plt.subplots()
    ax.bar(medias.keys(), medias.values())
    ax.set_ylabel("Pontuação média")
    ax.set_title("Comparação geral das dimensões")

    st.pyplot(fig)


'''
#===================================================
#                   POR VALENCIA
#===================================================
def detalhar_dimensao(df, atleta, id_col):
    linha = df[df[id_col] == atleta]
    dados = linha.select_dtypes(include="number").T
    dados.columns = ["Nota"]
    return dados

st.subheader("Detalhamento por dimensão")

st.markdown("### 🧠 Psicológico")
st.dataframe(detalhar_dimensao(df_psic, atleta, ID_COL))

st.markdown("### 🧠 Psicológico")
st.dataframe(detalhar_dimensao(df_psic, atleta, ID_COL))

st.markdown("### 🎯 Tático")
st.dataframe(detalhar_dimensao(df_tat, atleta, ID_COL))

st.markdown("### 💪 Físico")
st.dataframe(detalhar_dimensao(df_fis, atleta, ID_COL))
'''