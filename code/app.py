#streamlit run app.py --server.port 8501
import streamlit as st

def main():
    st.title('Dashboard')
    url_github = "https://github.com/wolfxweb/eng_machine_learning/raw/f0dd74b77a240c522383b7ef104bce11d61ae17c/docs/artefatos"
    url_grafico = f"{url_github}/graficos/pre_processamento"
    # Aba PreparacaoDados
    with st.sidebar:
        st.sidebar.title('Menu')
        tab_selected = st.radio('Selecione uma aba:', ['Preparacao Dados', 'Treinamento', 'Pipeline Aplicacao','  Apresentação'])
  

    if tab_selected == 'PreparacaoDados':
        st.header('Preparação de Dados')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Preparação de Dados.')
     
        # URL direta da imagem hospedada no GitHub
        boxplot_faixa_dinamica = f"{url_grafico}/boxplot_faixa_dinamica.png"
        st.image(boxplot_faixa_dinamica, caption='Exemplo de imagem na preparação de dados', use_column_width=True)

    # Aba Treinamento
    elif tab_selected == 'Treinamento':
        st.header('Treinamento')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Treinamento.')

    # Aba PipelineAplicacao
    elif tab_selected == 'PipelineAplicacao':
        st.header('Pipeline de Aplicação')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Pipeline de Aplicação.')
    
    elif tab_selected == 'Apresentação':
        st.header('Apresentação')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Pipeline de Aplicação.')
        # URL do arquivo PDF hospedado no OneDrive
        pdf_url = "https://1drv.ms/p/s!AtgitvPT0788g_lFaG6r4kMmh8Jdqg?e=QG7SK4"

        # Exibir o PDF usando um iframe
        st.write(f'<iframe src="{pdf_url}" width="700" height="500"></iframe>', unsafe_allow_html=True)










if __name__ == "__main__":
    main()
