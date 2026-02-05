import streamlit as st

#================================================
#       carregar a key da pagina Upload
#================================================
def carregar_key():
    chaves_df = [
    "psicologico_df",
    "tecnico_df",
    "tatico_df",
    "fisico_df"
    ]

    if not all (k in st.session_state for k in chaves_df):
        st.warning("Envie todos os arquivos na aba Arquivos antes de acessar o dashboard.")
        st.stop()
