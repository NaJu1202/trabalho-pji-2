import streamlit as st

from src.db.connection import ConnectionDB


class VacinasObrigatoriasPorPaisPage:
    def __init__(self) -> None:
        self.connection_db = ConnectionDB()

    def page(self):
        try:
            st.title(
                "Aqui você pode ver as vacinas obrigatorias filtrando por: País, continente e nome da vacina"
            )

            pais_filtrado = st.selectbox(
                label="Selecione o país",
                placeholder="Digite o nome do país",
                options=(self.connection_db.controler_pais.consultar_paises()),
            )

            continente_filtrado = st.selectbox(
                label="Selecione o continente",
                placeholder="Digite o nome do continente",
                options=(
                    self.connection_db.controler_continente.consultar_continentes()
                ),
            )

            nome_vacina_filtrado = st.text_input(
                label="Digite o nome da vacina",
                placeholder="Digite o nome da vacina",
                options=(self.connection_db.controler_vacinas.consultar_vacinas()),
            )

            if pais_filtrado:
                st.write(f"Selecionado: {pais_filtrado}")

                st.dataframe(
                    data=self.connection_db.controler_vacinas.pesquisar_vacinas_por_país(
                        nome_país=pais_filtrado
                    )
                )
            elif continente_filtrado:
                st.write(f"Selecionado: {continente_filtrado}")

                st.dataframe(
                    data=self.connection_db.controler_vacinas.pesquisar_vacinas_por_continente(
                        nome_continente=continente_filtrado
                    )
                )
            elif nome_vacina_filtrado:
                st.write(f"Selecionado: {nome_vacina_filtrado}")

                st.dataframe(
                    data=self.connection_db.controler_vacinas.pesquisar_vacinas_por_nome(
                        nome_vacina=nome_vacina_filtrado
                    )
                )

        except Exception as e:
            st.error(
                f"Ocorreu um erro inesperado | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )


if __name__ == "__main__":
    VacinasObrigatoriasPorPaisPage().page()
