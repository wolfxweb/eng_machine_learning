#streamlit run app.py --server.port 8501
import streamlit as st

def main():
    st.title('Dashboard')

    # Aba PreparacaoDados
    with st.sidebar:
        st.sidebar.title('Menu')
        tab_selected = st.radio('Selecione uma aba:', ['PreparacaoDados', 'Treinamento', 'PipelineAplicacao'])
  

    if tab_selected == 'PreparacaoDados':
        st.header('Preparação de Dados')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Preparação de Dados.')
      
        # Caminho para a imagem
        image_path = "./histograma.png"
        # Exibe a imagem
     #   st.image(image_path, caption='Exemplo de imagem na preparação de dados', use_column_width=True)

    # Aba Treinamento
    elif tab_selected == 'Treinamento':
        st.header('Treinamento')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Treinamento.')

    # Aba PipelineAplicacao
    elif tab_selected == 'PipelineAplicacao':
        st.header('Pipeline de Aplicação')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Pipeline de Aplicação.')

if __name__ == "__main__":
    main()
