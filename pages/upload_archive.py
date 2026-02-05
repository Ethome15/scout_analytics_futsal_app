import streamlit as st
from utils.read_archive import ler_arquivo

st.markdown('''# Arquivos 📄
Aqui você vai colocar os arquivos para a análise            
''')
st.sidebar.markdown("# Arquivos 📄")
    
def tipos_arquivos():
    categorias = {
        "Psicológico 🧠": "psicologico",
        "Técnico 🧩": "tecnico",
        "Tático 🎯": "tatico",
        "Físico 💪": "fisico"
    }

    for titulo, base_key in categorias.items():
        st.markdown(f"# {titulo}")

        upload = st.file_uploader(
            "Faça o upload aqui:",
            type=['csv','xlsx'],
            key=f"{base_key}_upload"
        )

        if upload:
            df = ler_arquivo(upload)
            if df is not None:
                st.session_state[f"{base_key}_df"] = df
                st.success("Arquivo carregado com sucesso")

tipos_arquivos()