import streamlit as st

from src.db.connection import ConnectionDB


class VacinasObrigatoriasPorPaisPage:
    def __init__(self) -> None:
        self.connection_db = ConnectionDB()

    def page(self):
        try:
            st.title("Aqui você pode ver as vacinas obrigatorias filtrando por País")

            pais_filtrado = st.selectbox(
                label="Selecione o país",
                placeholder="Digite o nome do país",
                options=(self.connection_db.controler_pais.consultar_paises()),
                key="pais-filtrado-pesquisa",
            )

            if pais_filtrado:
                resultado = (
                    self.connection_db.controler_vacinas.pesquisar_vacinas_por_país(
                        nome_país=pais_filtrado
                    )
                )

                if not resultado[1]:
                    st.write("Nenhuma vacina foi encontrada para o país selecionado.")
                else:
                    df = resultado[0]  # já é seu dataframe

                    configs = {
                        col: st.column_config.TextColumn(width="medium")
                        for col in df.columns
                    }

                    st.dataframe(
                        df,
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

                pais = st.selectbox(
                    label="Selecione o país",
                    placeholder="Digite o nome do país",
                    options=(self.connection_db.controler_pais.consultar_paises()),
                    key="pais-cadastro",
                )

                vacina = st.text_input(label="Nome da vacina obrigatória")
                grupo_de_risco = st.text_input(label="Grupo de risco")

                if pais and vacina and grupo_de_risco:
                    sucesso_cadastro = (
                        self.connection_db.controler_vacinas.cadastrar_vacina(
                            nome_vacina=vacina,
                            grupo_de_risco=grupo_de_risco,
                            id_pais=pais_filtrado,
                        )
                    )
                    if sucesso_cadastro:
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
