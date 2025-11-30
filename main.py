import streamlit as st

if __name__ == "__main__":
    st.set_page_config(page_title="VaciPass", page_icon="💉")

    pg = st.navigation(
        pages=[st.Page("src/pages/vacinas_obrigatorias_por_pais_page.py", icon="💉")]
    )

    pg.run()
