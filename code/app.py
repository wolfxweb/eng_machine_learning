#streamlit run app.py --server.port 8501
import streamlit as st

import pandas as pd
import pyarrow.parquet as pq
import io
import requests

def getTextGitHub(url):
    # Realizar uma solicitação HTTP para obter o conteúdo do arquivo
    response = requests.get(url)
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Exibir o conteúdo do arquivo
        content = response.text
        st.text_area("Conteúdo do DataFrame:", content, height=400)
    else:
        st.error(f"Erro ao obter o arquivo: {response.status_code}")
      


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
        st.markdown(info_describe)
        info_describe_anlise = """
            Analizando o resultado mostrado na tabela com a estatística descritiva
            - count: Todas as colunas têm 24.271 observações válidas, o que indica que não há valores nulos em nosso conjunto de dados.
            - mean: A média aritmética dos valores em cada coluna fornece uma ideia do valor médio de cada variável. Por exemplo, a média de game_event_id é aproximadamente 240.57.
            - std: O desvio padrão é uma medida de dispersão dos valores em relação à média. Quanto maior o desvio padrão, mais dispersos estão os dados em torno da média. Por exemplo, o desvio padrão de game_event_id é aproximadamente 148.51, indicando uma certa variabilidade nos valores dessa variável.
            - min: O valor mínimo em cada coluna indica o menor valor observado para cada variável. Por exemplo, o valor mínimo de game_event_id é 2.
            - 25% (Q1), 50% (Q2), 75% (Q3): Os percentis fornecem informações sobre a distribuição dos dados. Por exemplo, 25% das observações de game_event_id são menores que 102, 50% são menores que 244 (mediana) e 75% são menores que 355.
            - max: O valor máximo em cada coluna indica o maior valor observado para cada variável. Por exemplo, o valor máximo de game_event_id é 659.
        """
    
        st.markdown(info_describe_anlise)
     
        st.subheader("Valores Ausentes")
        info_valores_ausentes = """
            Com base na análise do resultado da tabela com a estatítica descritiva, podemos observar que todas as colunas têm a mesma contagem de observações, que é 24.271. 
            Isso indica que não há valores nulos ou faltantes neste conjunto de dados, pois todas as colunas possuem o mesmo número de observações não nulas.
        """
        st.markdown(info_valores_ausentes)
        
   
        st.write("Tabela com a estatística descritiva")
        st.write(df_dev.describe())
        
        st.subheader("Tamanho do conjunto de dados inicial")
        st.text(f"Quantidade de linhas: {df_dev.shape[0]}, Quantidade de colunas: {df_dev.shape[1]}")
       
        st.subheader("Conteúdo do arquivo colunas_iniciais.txt")
        colunas_iniciais_text = """
           Em resumo, o DataFrame fornecido contém informações sobre arremessos em jogos de basquete, com 24.271 entradas e 25 colunas.
           A maioria das colunas são numéricas, mas também há colunas categóricas e algumas com valores nulos. 
           A coluna `shot_made_flag` provavelmente representa o alvo para previsão, indicando se o arremesso foi bem-sucedido ou não.
           Análises adicionais podem ser realizadas para explorar tendências temporais, relações entre variáveis e distribuição de arremessos bem-sucedidos em diferentes áreas do campo. 
           Essas análises são essenciais para entender melhor o conjunto de dados e informar a construção de modelos de previsão ou outras análises específicas.
         """
        st.markdown(colunas_iniciais_text)
        url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/texto/colunas_iniciais.txt"
        getTextGitHub(url) 
       
        st.subheader("Conteúdo do arquivo colunas_data_filtered.txt")
        url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/texto/colunas_data_filtered.txt"
        colunas_data_filtered_text = """
           O DataFrame contém informações detalhadas sobre arremessos em jogos de basquete, com 20.285 entradas e 6 colunas.
           As colunas representam diferentes aspectos de cada arremesso, incluindo a posição (lat), tempo restante no jogo (minutes_remaining), período do jogo (period), indicação de se é playoff ou não (playoffs), distância do arremesso (shot_distance) e se o arremesso foi bem-sucedido ou não (shot_made_flag). 
           Todas as colunas têm dados não nulos, o que indica que não há necessidade de lidar com valores ausentes.
         """
        st.markdown(colunas_data_filtered_text)
        getTextGitHub(url) 
     
        st.subheader("Tamanho do conjunto de dados depois do pré-processamento (data_filtered.parquet)")
           
        # URL do DataFrame filtrado
        url_df_dev = "https://github.com/wolfxweb/eng_machine_learning/raw/main/data/processed/data_filtered.parquet"
        df_filtred = pd.read_parquet(url_df_dev) 
        st.text(f"Quantidade de linhas: {df_filtred.shape[0]}, Quantidade de colunas: {df_filtred.shape[1]}")
       
        st.subheader("Tabela com a estatística descritiva  (data_filtered.parquet)")
        data_filtered_text = """
           Analizando o resultado mostrado na tabela com a estatística descritiva do data set data_filtred       
            - lat (Latitude):** A média da latitude é de aproximadamente 33.98, com um desvio padrão relativamente pequeno de 0.066, indicando que os arremessos tendem a ocorrer em uma faixa estreita de latitudes.
            - minutes_remaining (Minutos Restantes):** A média de minutos restantes é de cerca de 5.10, com um desvio padrão de aproximadamente 3.42. Isso sugere uma distribuição variada do tempo restante nos arremessos.
            - period (Período):** A média do período é de cerca de 2.47, com a maioria dos arremessos ocorrendo nos períodos 1 a 3 (50% dos dados estão nesse intervalo). O período mínimo é 1 e o máximo é 7.
            - playoffs (Playoffs):** A média de playoffs indica que apenas cerca de 14.87% dos arremessos ocorrem durante os playoffs, pois o valor médio é 0. Isso sugere que a maioria dos arremessos é feita durante os jogos regulares da temporada.
            - shot_distance (Distância do Arremesso):** A média da distância do arremesso é de aproximadamente 10.22 pés, com um desvio padrão de 7.56 pés. Isso indica uma ampla variação nas distâncias dos arremessos, com alguns arremessos muito próximos da cesta e outros a uma distância significativa.
            - shot_made_flag (Indicador de Arremesso Bem-Sucedido):** A média do indicador de arremesso bem-sucedido é de aproximadamente 0.48, o que sugere que aproximadamente metade dos arremessos foram bem-sucedidos. Isso é apoiado pelo fato de que o valor mínimo é 0 e o valor máximo é 1, indicando que a coluna contém valores binários representando se um arremesso foi ou não bem-sucedido.
          """
        st.markdown(data_filtered_text)
        st.write(df_filtred.describe()) 


        st.subheader("Faixa Dinâmica das variaveis")
        boxplot_faixa_dinamica = f"{url_grafico}/boxplot_faixa_dinamica.png"
        st.image(boxplot_faixa_dinamica, caption='Gráfico Box Plot - Faixa Dinâmica das variaveis', use_column_width=True)

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
