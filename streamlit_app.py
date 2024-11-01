import streamlit as st
from login import login_page
from avaliacao_abcd import abcd_page
from func_data import func_data_page
from alter_nota import func_data_nota

# Verifica se o usuário está logado
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Obtém parâmetros da URL com st.query_params
query_params = st.query_params
pagina = query_params.get("page", ["login"])[0]  # Define login como padrão

# Lógica de navegação baseada no estado de login
if not st.session_state['logged_in'] and pagina != "login":
    st.experimental_set_query_params(page="login")  # Força a página de login
    login_page()
else:
    # Seletor de páginas na barra lateral
    st.sidebar.title("Navegação")
    pagina_selecionada = st.sidebar.selectbox(
        "Escolha a página",
        ["Avaliação ABCD", "Funcionários Data", "Lista de Avaliados"]
    )

    # Navega para a página selecionada
    if pagina_selecionada == "Avaliação ABCD" or pagina == "avaliacao_abcd":
        abcd_page()
    #elif pagina_selecionada == "Funcionários Data":
        func_data_page()
    elif pagina_selecionada == "Lista de Avaliados":
        func_data_nota()