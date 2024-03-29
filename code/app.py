#streamlit run app.py --server.port 8501
import streamlit as st

def main():
    st.title('Dashboard')
    #url para pegar os artefatos que estão no github
    url_github = "https://github.com/wolfxweb/eng_machine_learning/raw/f0dd74b77a240c522383b7ef104bce11d61ae17c/docs/artefatos/"
    url_grafico = f"{url_github}/graficos/pre_processamento"
    
    # Aba PreparacaoDados
    with st.sidebar:
        st.sidebar.title('Menu')
        tab_selected = st.radio('Selecione uma aba:', ['Processamento', 'Treinamento', 'PipelineAplicacao','Apresentação'])
  

    if tab_selected == 'PreparacaoDados':
        st.header('Processamento de Dados')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Preparação de Dados.')
  
  
  
        boxplot_faixa_dinamica = f"{url_grafico}/boxplot_faixa_dinamica.png"
        # Exibir a imagem no Streamlit
        st.image(boxplot_faixa_dinamica, caption='Exemplo de imagem na preparação de dados', use_column_width=True)

    # Aba Treinamento
    elif tab_selected == 'Treinamento':
        st.header('Treinamento')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Treinamento.')

    # Aba PipelineAplicacao
    elif tab_selected == 'PipelineAplicacao':
        st.header('Pipeline de Aplicação')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Pipeline de Aplicação.')
        
    elif tab_selected == "Apresentação":
        st.header('Apresentação')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Pipeline de Aplicação.')
        # Código HTML do iframe
        iframe_code = """
        <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ6QufhOXcTmaqc2hgUJC2ACPLgR74Kh1j08fg40Zmzw5vLxgMCJFTndHp92sVMhg/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """

        # Exibir o iframe
        st.write(iframe_code, unsafe_allow_html=True)
        
        
        
        
if __name__ == "__main__":
    main()
