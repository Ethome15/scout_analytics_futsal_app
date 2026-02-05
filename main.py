import streamlit as st

st.set_page_config(page_title="Scout Futsal", page_icon=":soccer:")

# Define the pages
Dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon="📊")
Upload_arquivo = st.Page("pages/upload_archive.py", title="Arquivos", icon="📄")

# Set up navigation
pg = st.navigation([Dashboard, Upload_arquivo])

# Run the selected page
pg.run()