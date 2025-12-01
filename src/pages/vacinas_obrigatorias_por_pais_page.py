import pandas as pd
import requests
import streamlit as st

from src.db.connection import ConnectionDB


class VacinasObrigatoriasPorPaisPage:
    def __init__(self) -> None:
        self.connection_db = ConnectionDB()

    def page(self):
        try:
            st.title("Aqui você pode ver as vacinas obrigatorias filtrando por País")

            response_paises = requests.get("http://localhost:8000/paises").json()

            pais_filtrado = st.selectbox(
                label="Selecione o país",
                placeholder="Digite o nome do país",
                options=[""] + response_paises["paises"],
                key="pais-filtrado-pesquisa",
            )

            if pais_filtrado:
                response = requests.get(
                    f"http://localhost:8000/vacinas?pais={pais_filtrado}"
                ).json()

                resultado = response.get(pais_filtrado)[1]

                if not resultado:
                    st.write("Nenhuma vacina foi encontrada para o país selecionado.")
                else:
                    resultado = pd.DataFrame(response.get(pais_filtrado)[0])
                    configs = {
                        col: st.column_config.TextColumn(width="medium")
                        for col in resultado.columns
                    }

                    st.dataframe(
                        resultado,
                        hide_index=True,
                        column_config=configs,
                    )

            st.markdown(
                """
            <style>
            .st-key-btn-cadastro-de-vacina {
                display: block;
                margin: 0 auto;
            }
            </style>
            """,
                unsafe_allow_html=True,
            )

            btn_cadastro = st.button(
                label="Deseja cadastrar uma vacina obrigatoria?",
                key="btn-cadastro-de-vacina",
            )
            if btn_cadastro:
                st.title("Cadastrar uma nova vacina: ")

                pais = pais_filtrado = st.selectbox(
                    label="Selecione o país",
                    placeholder="Digite o nome do país",
                    options=response_paises["paises"],
                    key="pais-cadastro",
                )

                vacina = st.text_input(label="Nome da vacina obrigatória")
                grupo_de_risco = st.text_input(label="Grupo de risco")

                st.markdown(
                """
                <style>
                .st-key-btn-confirmar-cadastro-de-vacina {
                    display: block;
                    margin: 0 auto;
                }
                </style>
                """,
                    unsafe_allow_html=True,
                )

                btn_cadastro = st.button(
                    label="Consfirmar cadastro",
                    key="btn-confirmar-cadastro-de-vacina",
                )

                if pais and vacina and grupo_de_risco:
                    url = "http://localhost:8000/vacinas"

                    payload = {
                        "nome": vacina.title().strip(),
                        "grupo": grupo_de_risco,
                        "pais": pais,
                    }

                    response = requests.post(url, json=payload)

                    if response.ok:
                        st.success("Vacina cadastrada com sucesso!")
                    else:
                        st.error("Ocorreu um erro inesperado ao cadastrar a vacina.")
        except Exception as e:
            st.error(
                f"Ocorreu um erro inesperado | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )


if __name__ == "__main__":
    teste = VacinasObrigatoriasPorPaisPage()
    teste.page()
