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
            )

            if pais_filtrado:
                st.write(f"Selecionado: {pais_filtrado}")

                resultado = (
                    self.connection_db.controler_vacinas.pesquisar_vacinas_por_país(
                        nome_país=pais_filtrado
                    )
                )

                if not resultado:
                    st.write("Nenhuma vacina foi encontrada para o país selecionado.")
                else:
                    st.dataframe(data=resultado)

            st.title("Cadastrar uma nova vacina: ")

            pais = pais_filtrado = st.selectbox(
                label="Selecione o país",
                placeholder="Digite o nome do país",
                options=(self.connection_db.controler_pais.consultar_paises()),
            )

            continente = st.selectbox(
                label="Selecione o continente",
                placeholder="Digite o nome do continente",
                options=(
                    self.connection_db.controler_continente.consultar_continentes()
                ),
            )

            vacina = st.text_input(label="Nome da vacina obrigatória")
            grupo_de_risco = st.text_input(label="Grupo de risco")

            if pais and continente and vacina and grupo_de_risco:
                sucesso_cadastro = (
                    self.connection_db.controler_vacinas.cadastrar_vacina(
                        nome_vacina=vacina,
                        grupo_de_risco=grupo_de_risco,
                        id_pais=pais_filtrado,
                        id_continente=continente,
                    )
                )
                if sucesso_cadastro:
                    st.success("Vacina cadastrada com sucesso!")
                    st.stop()
                else:
                    st.error("Ocorreu um erro inesperado ao cadastrar a vacina.")
                    st.stop()

            st.rerun()

        except Exception as e:
            st.error(
                f"Ocorreu um erro inesperado | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )


if __name__ == "__main__":
    teste = VacinasObrigatoriasPorPaisPage()
    teste.page()
