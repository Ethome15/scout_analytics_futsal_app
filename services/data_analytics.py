import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.validations import carregar_key

#AQUI VAI FICAR OS CALCULOS
carregar_key()
#================================================
#         Puxar os dados dos arquivos
#================================================

df_psic = st.session_state["psicologico_df"]
df_tec = st.session_state["tecnico_df"]
df_tat = st.session_state["tatico_df"]
df_fis = st.session_state["fisico_df"]

#================================================
#         definir os nomes dos atletas
#================================================
def nomes_atletas():
    ID_COL = "NOME"

    atletas = pd.concat([
        df_psic[ID_COL],
        df_tec[ID_COL],
        df_tat[ID_COL],
        df_fis[ID_COL],
    ]).dropna().unique()

    return atletas.tolist()


#================================================
#     Fazer a conta das Medias por valencia
#================================================
def conta_media_geral(df):
    return df.select_dtypes(include="number").mean().mean()

def media():
    return {
        "Psicológico": conta_media_geral(df_psic),
        "Técnico": conta_media_geral(df_tec),
        "Tático": conta_media_geral(df_tat),
        "Físico": conta_media_geral(df_fis),
    }

def mostrar_medias():
    medias = media()

    st.markdown(f'Média Geral Psicológico: {round(medias["Psicológico"],2)}')
    st.markdown(f'Média Geral Técnico: {round(medias["Técnico"],2)}')
    st.markdown(f'Média Geral Tático: {round(medias["Tático"],2)}')
    st.markdown(f'Média Geral Físico: {round(medias["Físico"],2)}')

#===================================================
#          Análise e Média Individual
#===================================================

atletas = nomes_atletas()

def media_atleta(df, atleta):
    ID_COL = "NOME"
    linha = df[df[ID_COL] == atleta]

    if linha.empty:
        return None

    return linha.select_dtypes(include="number").mean(axis=1).iloc[0]

def escolha_do_atleta():
    atletas = nomes_atletas()

    atleta = st.selectbox(
        "Selecione o atleta",
        atletas,
        key="select_atleta"
    )
    return atleta

def media_individual():
    jogador = escolha_do_atleta()
    perfil = {
        "Psicológico": media_atleta(df_psic, jogador),
        "Técnico": media_atleta(df_tec, jogador),
        "Tático": media_atleta(df_tat, jogador),
        "Físico": media_atleta(df_fis, jogador),
    }
    st.subheader(f"Médias do atleta: {jogador}")
    st.markdown(f'Avaliação Psicológica: {round(perfil["Psicológico"],2)}')
    st.markdown(f'Avaliação Técnico: {round(perfil["Técnico"],2)}')
    st.markdown(f'Avaliação Tático: {round(perfil["Tático"],2)}')
    st.markdown(f'Avaliação Físico: {round(perfil["Físico"],2)}')

    #===================================================
    #                     RADAR
    #===================================================

    labels = list(perfil.keys())
    valores = list(perfil.values())

        # fecha o gráfico
    valores += valores[:1]
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1)

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))

    ax.plot(angles, valores)
    ax.fill(angles, valores, alpha=0.25)

    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
    ax.set_ylim(0, 10)
    ax.set_title(f"Perfil Geral do Atleta - {jogador}")

    st.pyplot(fig)
