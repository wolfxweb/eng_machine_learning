#streamlit run app.py --server.port 8501
import streamlit as st

import pandas as pd
import pyarrow.parquet as pq
import io
import requests


def main():
    st.title('Dashboard')
    #url para pegar os artefatos que estão no github
    url_github = "https://github.com/wolfxweb/eng_machine_learning/raw/f0dd74b77a240c522383b7ef104bce11d61ae17c/docs/artefatos/"
    url_grafico = f"{url_github}/graficos/pre_processamento"
    
    # Aba PreparacaoDados
    with st.sidebar:
        st.sidebar.title('Menu')
        tab_selected = st.radio('Selecione uma aba:', ['Processamento de Dados', 'Treinamento', 'PipelineAplicacao','Apresentação'])
  

    if tab_selected == 'Processamento de Dados':
        st.header('Preparação de Dados')
        st.write('Este é um exemplo de aplicação Streamlit com a aba de Preparação de Dados.')
  
  # URL do arquivo CSV no GitHub
        url = 'https://raw.githubusercontent.com/seu_usuario/seu_repositório/seu_caminho/seu_arquivo.csv'

        ## URL do arquivo parquet no GitHub
        url = 'https://github.com/wolfxweb/eng_machine_learning/raw/main/data/processed/data_filtered.parquet'

        # Baixa o conteúdo do arquivo parquet
        response = requests.get(url)
        buffer = io.BytesIO(response.content)

        # Lê o arquivo parquet em um DataFrame
        df = pq.read_table(buffer).to_pandas()

        # Exibe o DataFrame
        st.write(df)
  
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
        <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQXW0aUksH1cjl28nhkk7sh6ITmPdMV1bYxnCPrfQFeC9WDBsHfR2lQkjB2Be4la0R9PcmvIsoLHFUF/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """

        # Exibir o iframe
        st.write(iframe_code, unsafe_allow_html=True)
        
        
        
        
if __name__ == "__main__":
    main()
