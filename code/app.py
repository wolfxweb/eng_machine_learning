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
        st.write('Uma exploração de dados é uma etapa crucial em qualquer projeto de análise de dados ou aprendizado de máquina. Durante essa fase, vamos examina o conjunto de dados para entender sua estrutura, características e comportamentos subjacentes. ')
  
        st.subheader("Visão Geral do Conjunto de Dados:")
        ## URL do data frame de desenvolvimento
        url_df_dev = "https://github.com/wolfxweb/eng_machine_learning/raw/main/data/raw/dataset_kobe_dev.parquet"

        df_dev = pd.read_parquet(url_df_dev)
        st.subheader("Análise estatística descritiva")
        info_describe = """
            Nesta análise estamos utilizando a função describe().
            Ela calcula várias estatísticas descritivas, incluindo:
            - Contagem: o número de observações não nulas em cada coluna.
            - Média: a média aritmética dos valores em cada coluna.
            - Desvio padrão: uma medida de dispersão dos valores em cada coluna em relação à média.
            - Mínimo: o valor mínimo em cada coluna.
            - 25º percentil (Q1): o valor abaixo do qual 25% dos dados caem em cada coluna.
            - 50º percentil (mediana ou Q2): o valor abaixo do qual 50% dos dados caem em cada coluna.
            - 75º percentil (Q3): o valor abaixo do qual 75% dos dados caem em cada coluna.
            - Máximo: o valor máximo em cada coluna.
        """
        st.write(info_describe)
        info_describe_anlise = """
            Analizando o resultado mostrado na tabela com a estatística descritiva
            - count: Todas as colunas têm 24.271 observações válidas, o que indica que não há valores nulos em nosso conjunto de dados.
            - mean: A média aritmética dos valores em cada coluna fornece uma ideia do valor médio de cada variável. Por exemplo, a média de game_event_id é aproximadamente 240.57.
            - std: O desvio padrão é uma medida de dispersão dos valores em relação à média. Quanto maior o desvio padrão, mais dispersos estão os dados em torno da média. Por exemplo, o desvio padrão de game_event_id é aproximadamente 148.51, indicando uma certa variabilidade nos valores dessa variável.
            - min: O valor mínimo em cada coluna indica o menor valor observado para cada variável. Por exemplo, o valor mínimo de game_event_id é 2.
            - 25% (Q1), 50% (Q2), 75% (Q3): Os percentis fornecem informações sobre a distribuição dos dados. Por exemplo, 25% das observações de game_event_id são menores que 102, 50% são menores que 244 (mediana) e 75% são menores que 355.
            - max: O valor máximo em cada coluna indica o maior valor observado para cada variável. Por exemplo, o valor máximo de game_event_id é 659.
        """
        st.write(info_describe_anlise)
        st.write("Tabela com a estatística descritiva.")
        st.write(df_dev.describe())
        
        st.subheader("Tamanho do conjunto de dados inicial")
        st.write(f"Quantidade de linhas {df_dev.shape[0]}")
        st.write(f"Quantidade de colunas {df_dev.shape[1]}") 
        
        
        
        
      #  st.write("Data frame antes do processamento")
     #   st.write(df_dev)
   #     st.write(df_dev)
  
        ## URL do arquivo parquet no GitHub
     #   url = 'https://github.com/wolfxweb/eng_machine_learning/raw/main/data/processed/data_filtered.parquet'

        # Baixa o conteúdo do arquivo parquet
     #   response = requests.get(url)
      #  buffer = io.BytesIO(response.content)

        # Lê o arquivo parquet em um DataFrame
      #  df = pq.read_table(buffer).to_pandas()

        # Exibe o DataFrame
      #  st.write(df)
  
      #  boxplot_faixa_dinamica = f"{url_grafico}/boxplot_faixa_dinamica.png"
        # Exibir a imagem no Streamlit
      #  st.image(boxplot_faixa_dinamica, caption='Exemplo de imagem na preparação de dados', use_column_width=True)

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
