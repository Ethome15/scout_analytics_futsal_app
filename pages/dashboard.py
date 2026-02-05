import streamlit as st
from utils.validations import carregar_key
from services.graphics import grafico_media_geral
from services.data_analytics import mostrar_medias, media_individual


st.markdown('''# Dashboard 📊''')
st.sidebar.markdown("# Dashboard 📊")

carregar_key()

box_media_geral = st.expander(label="Media Geral do Grupo por Valencia")
box_analise_atleta = st.expander(label="Analise Geral do Atleta")

with box_media_geral:
    mostrar_medias()
    grafico_media_geral()

with box_analise_atleta:
    media_individual()