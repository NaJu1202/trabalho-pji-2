import streamlit as st

from src.db.connection import ConnectionDB


class VacinasObrigatoriasPorPaisPage:
    def __init__(self) -> None:
        # conexão persistente entre reloads
        if "connection_db" not in st.session_state:
            st.session_state.connection_db = ConnectionDB()

        self.connection_db = st.session_state.connection_db

    def page(self):
        try:
            st.title("Aqui você pode ver as vacinas obrigatorias filtrando por País")

            pais_filtrado = st.selectbox(
                label="Selecione o país",
                placeholder="Digite o nome do país",
                options=self.connection_db.controler_pais.consultar_paises(),
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
                    df = resultado[0]
                    configs = {
                        col: st.column_config.TextColumn(width="medium")
                        for col in df.columns
                    }
                    st.dataframe(df, hide_index=True, column_config=configs)

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

            # botão de cadastro
            btn_cadastro = st.button(
                "Deseja cadastrar uma vacina obrigatoria?", key="btn-cadastro-de-vacina"
            )

            if btn_cadastro:
                with st.form("form_cadastro_vacina"):
                    pais = st.selectbox(
                        "Selecione o país",
                        options=self.connection_db.controler_pais.consultar_paises(),
                    )

                    vacina = st.text_input("Nome da vacina obrigatória")
                    grupo_de_risco = st.text_input("Grupo de risco")

                    st.markdown(
                        """
                    <style>
                    .st-key-btn-confirmar-cadastro {
                        display: block;
                        margin: 0 auto;
                    }
                    </style>
                    """,
                        unsafe_allow_html=True,
                    )

                    btn_confirmar = st.form_submit_button(
                        "Confirmar cadastro", key="btn-confirmar-cadastro"
                    )

                    if btn_confirmar:
                        sucesso_cadastro = (
                            self.connection_db.controler_vacinas.cadastrar_vacina(
                                nome_vacina=vacina,
                                grupo_de_risco=grupo_de_risco,
                                pais=pais,
                            )
                        )
                        if sucesso_cadastro:
                            st.success("Vacina cadastrada com sucesso!")
                        else:
                            st.error("Erro ao cadastrar vacina.")

        except Exception as e:
            st.error(f"Erro inesperado: {e.__traceback__.tb_lineno} | {e}")


if __name__ == "__main__":
    VacinasObrigatoriasPorPaisPage().page()
