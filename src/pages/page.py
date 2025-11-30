import streamlit as st

from src.db.connection import ConnectionDB


def page():
    try:
        st.set_page_config(page_title="Vacinas Obrigatórias", page_icon="💉")

        connection_db = ConnectionDB()

        st.title("Aqui você pode ver as vacinas obrigatorias para viagens por país")

        st.selectbox(
            label="Selecione o país",
            options=(connection_db.controler_pais.consultar_paises()),
        )

    except Exception as e:
        st.error(
            f"Ocorreu um erro inesperado | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
        )
