# streamlit run app.py --server.port 8501
import streamlit as st

import pandas as pd
import pyarrow.parquet as pq
import io
import requests
import nbformat
from nbconvert import PythonExporter

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

def exibir_codigo_notebook(notebook_url):

    # Baixar o conteúdo do arquivo Jupyter Notebook
    response = requests.get(notebook_url)
    notebook_content = response.text

    # Carregar o notebook usando nbformat
    notebook = nbformat.reads(notebook_content, as_version=4)

    # Converter o notebook para código Python
    python_exporter = PythonExporter()
    python_code, _ = python_exporter.from_notebook_node(notebook)

    # Exibir o código Python no Streamlit
    st.code(python_code)


def setTextImagem(info_describe,url_imagem, titulo ):
    st.markdown(info_describe)
      # Mostrar a imagem no Streamlit
    st.image(f"https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/graficos/treinamento/{url_imagem}", caption=titulo)
        
def main():
    st.title('Dashboard')
    # url para pegar os artefatos que estão no github
    url_github = "https://github.com/wolfxweb/eng_machine_learning/raw/f0dd74b77a240c522383b7ef104bce11d61ae17c/docs/artefatos/"
    url_grafico = f"{url_github}/graficos/pre_processamento"
    github_image_url = "https://github.com/wolfxweb/eng_machine_learning/raw/main/docs/artefatos/graficos/pre_processamento/"
    # Aba PreparacaoDados
    with st.sidebar:
        st.sidebar.title('Menu')
        tab_selected = st.radio('Selecione uma aba:', ['Processamento de Dados', 'Treinamento', 'PipelineAplicacao','Apresentação'])

    if tab_selected == 'Processamento de Dados':
        st.header('Preparação de Dados')
        st.write('Uma exploração de dados é uma etapa crucial em qualquer projeto de análise de dados ou aprendizado de máquina. Durante essa fase, vamos examina o conjunto de dados para entender sua estrutura, características e comportamentos subjacentes. ')

        st.subheader("Visão Geral do Conjunto de Dados:")
        ## URL do data frame de desenvolvimento

        url_df_dev  = "https://github.com/wolfxweb/eng_machine_learning/raw/main/data/raw/dataset_kobe_prod.parquet"

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
        st.write("Tabela com a estatística descritiva") 
        url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/texto/colunas_iniciais.txt"
        getTextGitHub(url) 

        st.subheader("Conteúdo do arquivo colunas_data_filtered.txt")
        #   url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/texto/colunas_data_filtered.txt"
        url= "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/texto/colunas_data_filtered.txt"
        colunas_data_filtered_text = """
           O DataFrame contém informações detalhadas sobre arremessos em jogos de basquete, com 20.285 entradas e 6 colunas.
           As colunas representam diferentes aspectos de cada arremesso, incluindo a posição (lat), tempo restante no jogo (minutes_remaining), período do jogo (period), indicação de se é playoff ou não (playoffs), distância do arremesso (shot_distance) e se o arremesso foi bem-sucedido ou não (shot_made_flag). 
           Todas as colunas têm dados não nulos, o que indica que não há necessidade de lidar com valores ausentes.
         """
        st.markdown(colunas_data_filtered_text)
        getTextGitHub(url) 

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
        data_filtered_text = """
           Resultado da Análise Estatística Descritiva
          Analizando o resultado mostrado na tabela com a estatística descritiva do data set data_filtred:
          - **Latitude (lat):** A média da latitude é de aproximadamente 0.544, com um desvio padrão relativamente pequeno de 0.067, indicando que os arremessos tendem a ocorrer em uma faixa estreita de latitudes.
          - **Longitude (lon):** A média da longitude é de aproximadamente 0.438, com um desvio padrão relativamente pequeno de 0.066, indicando que os arremessos tendem a ocorrer em uma faixa estreita de longitudes.
          - **Minutos Restantes (minutes_remaining):** A média de minutos restantes é de cerca de 11.0, com um desvio padrão de aproximadamente 0.0. Isso sugere uma distribuição variada do tempo restante nos arremessos.
          - **Período (period):** A média do período é de cerca de 6.0, com a maioria dos arremessos ocorrendo no período 6. O período mínimo é 6 e o máximo é 6.
          - **Playoffs (playoffs):** A média de playoffs indica que todos os arremessos ocorrem durante os playoffs, pois o valor médio é 1. Isso sugere que os arremessos estão concentrados nos jogos dos playoffs.
          - **Distância do Arremesso (shot_distance):** A média da distância do arremesso é de aproximadamente 50.0 pés, com um desvio padrão de 0.0 pés. Isso indica que a distância dos arremessos é consistente.
          - **Flag de Arremesso Convertido (shot_made_flag):** A média do indicador de arremesso bem-sucedido é de aproximadamente 1.0, o que sugere que todos os arremessos foram bem-sucedidos. Isso é apoiado pelo fato de que o valor mínimo é 1 e o valor máximo é 1, indicando que a coluna contém valores binários representando se um arremesso foi ou não bem-sucedido.
        """
        st.markdown(data_filtered_text)

        url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/docs/artefatos/texto/faixa_dinamica.txt"
        getTextGitHub(url) 

        boxplot_faixa_dinamica = f"{github_image_url}/boxplot_faixa_dinamica.png"
        st.image(boxplot_faixa_dinamica, caption='Gráfico Box Plot - Faixa Dinâmica das variaveis', use_column_width=True)

        st.subheader("Matriz de correlação") 
        matriz_text = """
          Uma matriz de correlação é uma tabela que mostra os coeficientes de correlação entre várias variáveis. Cada célula na tabela representa o coeficiente de correlação entre duas variáveis. O coeficiente de correlação quantifica o grau de relação linear entre duas variáveis e varia de -1 a 1. 
          - Um valor de 1 indica uma correlação perfeita positiva, o que significa que as duas variáveis têm uma relação linear positiva perfeita. Isso significa que quando uma variável aumenta, a outra também aumenta na mesma proporção.
          - Um valor de -1 indica uma correlação perfeita negativa, o que significa que as duas variáveis têm uma relação linear negativa perfeita. Isso significa que quando uma variável aumenta, a outra diminui na mesma proporção.
          - Um valor de 0 indica ausência de correlação linear entre as variáveis. Isso significa que as variáveis ​​não têm uma relação linear clara entre si.
        """
        st.markdown(matriz_text)
        boxplot_faixa_dinamica = f"{github_image_url}/matriz_correlacao.png"
        st.image(boxplot_faixa_dinamica, caption='Matriz de correlação', use_column_width=True)

        st.subheader("Matriz de Dispersão")
        matriz_dispersao_text = """
         Essa matriz é útil para identificar padrões de correlação, tendências e possíveis associações entre as variáveis em um conjunto de dados. Cada gráfico de dispersão na matriz mostra como duas variáveis estão relacionadas entre si, permitindo uma rápida visualização das relações lineares ou não lineares.
         Ao examinar uma matriz de dispersão, aqui estão algumas interpretações comuns:
          - Padrões de correlação: Se os pontos em um gráfico de dispersão mostrarem uma tendência clara, isso pode indicar uma correlação entre as variáveis. Por exemplo, se os pontos formarem uma linha diagonal ascendente, isso sugere uma correlação positiva entre as duas variáveis.
          - Distribuições marginais: Além dos gráficos de dispersão, a matriz de dispersão também exibe as distribuições marginais de cada variável ao longo da diagonal principal. Isso permite verificar as distribuições univariadas das variáveis.
          - Identificação de outliers: A matriz de dispersão pode ajudar a identificar outliers ou valores extremos em um conjunto de dados. Pontos que estão longe da tendência geral nos gráficos de dispersão podem ser considerados outliers.
          - Multicolinearidade: Ao examinar os gráficos de dispersão, é possível identificar multicolinearidade, que é a presença de correlações altas entre duas ou mais variáveis independentes. Isso é importante na construção de modelos preditivos, pois pode afetar a interpretação dos coeficientes de regressão.
        """
        st.markdown(matriz_dispersao_text)             
        boxplot_faixa_dinamica = f"{github_image_url}/scatter_matrix.png"
        st.image(boxplot_faixa_dinamica, caption='Matriz de Dispersão', use_column_width=True)

        st.subheader("Histograma  das variaveis")
        histograma_text = """
            Um histograma é um gráfico de barras que representa a distribuição de uma variável quantitativa. Ele divide os dados em intervalos chamados de "bins" e conta quantas observações caem em cada bin. Essas contagens são então representadas graficamente como barras, onde a altura de cada barra indica a frequência ou a densidade das observações naquele bin. 
            Ao interpretar um histograma, aqui estão algumas informações importantes que podemos extrair:
            - Forma da distribuição: A forma geral do histograma fornece informações sobre a distribuição dos dados. Por exemplo, uma distribuição normal terá uma forma de sino, enquanto uma distribuição assimétrica pode ter uma cauda longa em uma direção.
            - Centralidade: O centro da distribuição pode ser identificado observando onde a maioria das observações está concentrada ao longo do eixo horizontal. Isso nos dá uma ideia da média ou da mediana dos dados.
            - Dispersão: A dispersão dos dados pode ser inferida observando a largura e a altura das barras no histograma. Uma distribuição mais dispersa terá barras mais largas e mais curtas, enquanto uma distribuição mais concentrada terá barras mais estreitas e mais altas.
            - Outliers: Observações incomuns ou outliers podem ser identificados como valores que se destacam significativamente do restante da distribuição. Esses valores aparecerão como barras solitárias ou isoladas nos extremos do histograma.
            - Simetria e assimetria: A simetria da distribuição pode ser observada visualmente no histograma. Distribuições simétricas terão barras distribuídas uniformemente em ambos os lados da média, enquanto distribuições assimétricas terão barras mais concentradas em um lado.
        """
        st.markdown(histograma_text)   

        boxplot_faixa_dinamica = f"{github_image_url}/histograma.png"
        st.image(boxplot_faixa_dinamica, caption='Histograma  das variaveis', use_column_width=True) 

        url_df_original  =  "https://github.com/wolfxweb/eng_machine_learning/raw/main/data/raw/dataset_kobe_dev.parquet"
        df_original= pd.read_parquet(url_df_original)
        st.subheader("Data Frame original") 
        st.write(df_original)

        st.subheader("Data Frame Dev")
        st.write(df_filtred)
       
        url_df_teste  = "https://github.com/wolfxweb/eng_machine_learning/raw/main/data/raw/dataset_kobe_prod.parquet"

        df_teste= pd.read_parquet(url_df_teste)
        st.subheader("Data Frame Filtrado Prod")
        st.write(df_teste)  
        
        st.subheader("Notebook da Preparaçã dos dados")
        notebook_url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/code/PreparacaoDados.ipynb"
        exibir_codigo_notebook(notebook_url)
    # Aba Treinamento
    elif tab_selected == 'Treinamento':
        st.header('Treinamento')
        info_describe = """
            Treinamento de modelos de classificação (Regressão Logística e RandomForestClassifier) para prever se um arremesso de basquete foi bem-sucedido ou não. Aqui está uma explicação passo a passo do que está sendo feito:
            - Importação de Bibliotecas: Importamos todas as bibliotecas necessárias, incluindo mlflow, pandas, scikit-learn, pycaret, matplotlib e numpy.
            - Carregamento dos Dados: Carregamos os dados de treinamento e teste de arquivos parquet.
            - Configuração do MLflow: Definimos o experimento no MLflow, verificamos se ele existe e, se não, criamos um novo. Configuramos também o repositório de rastreamento do MLflow para usar o SQLite.
            - Treinamento dos Modelos: Usamos o PyCaret para configurar o ambiente de treinamento, definindo os dados de treinamento, o tamanho do conjunto de treinamento e o nome do experimento. Em seguida, criamos modelos de Regressão Logística e RandomForestClassifier e finalizamos o ambiente.
            - Avaliação dos Modelos: Fazemos previsões usando os modelos treinados nos dados de teste e calculamos métricas de avaliação, como Log Loss e F1 Score, para ambos os modelos.
            - Seleção do Melhor Modelo: Determinamos o melhor modelo com base no valor mais alto do F1 Score.
            - Registro do Melhor Modelo: Registramos a versão do melhor modelo no MLflow.
            - Plotagem das Métricas: Criamos um gráfico de barras mostrando o Log Loss e o F1 Score para cada modelo.
            - Salvar o Gráfico: Salvamos o gráfico como um arquivo de imagem e registramos este artefato no MLflow.

        """
        st.markdown(info_describe)
        info_describe = """
            O processo de validação cruzada é uma técnica fundamental na avaliação de modelos de aprendizado de máquina e na seleção de hiperparâmetros. 
            - Avaliação do desempenho do modelo: A validação cruzada fornece uma estimativa mais robusta do desempenho do modelo do que uma única divisão treino-teste. Isso ocorre porque ela divide os dados em diferentes conjuntos de treinamento e teste e calcula a métrica de avaliação (como precisão, recall, F1-score, etc.) média em várias iterações.
            - Redução de variância: A validação cruzada ajuda a reduzir a variância na estimativa do desempenho do modelo. Isso ocorre porque ela utiliza múltiplas divisões dos dados, o que reduz a dependência do desempenho do modelo em uma única divisão específica dos dados.
            - Seleção de modelo: A validação cruzada pode ser usada para comparar o desempenho de diferentes modelos. Ao aplicar a validação cruzada a vários modelos, podemos identificar qual modelo tem o melhor desempenho médio em dados não vistos.
            - Seleção de hiperparâmetros: Além de selecionar o melhor modelo, a validação cruzada pode ser usada para ajustar os hiperparâmetros do modelo. Ao aplicar a validação cruzada com diferentes configurações de hiperparâmetros, podemos identificar os valores que produzem o melhor desempenho médio em dados não vistos.

        """
        st.markdown(info_describe)
        info_describe = """
           A curva de validação e a curva de aprendizado são ferramentas importantes para entender como o modelo foi treinado e para diagnosticar possíveis problemas durante o processo de treinamento. Aqui está como cada uma delas pode nos ajudar:
           Curva de Validação:
           - A curva de validação mostra como o desempenho do modelo varia em relação a diferentes valores de um hiperparâmetro.
           - Ela nos permite identificar se o modelo está sofrendo de underfitting ou overfitting em relação a um hiperparâmetro específico.
           - Se a curva de validação mostrar que o desempenho do modelo é baixo tanto no conjunto de treinamento quanto no conjunto de validação, isso pode indicar underfitting, sugerindo que o modelo é muito simples para capturar a complexidade dos dados.
           - Se a curva de validação mostrar uma grande diferença entre o desempenho no conjunto de treinamento e no conjunto de validação, isso pode indicar overfitting, sugerindo que o modelo está memorizando os dados de treinamento em vez de aprender padrões gerais.
           
        """
        st.markdown(info_describe)
        info_describe = """
           Curva de Aprendizado:
           - A curva de aprendizado mostra como o desempenho do modelo varia em relação ao tamanho do conjunto de treinamento.
           - Ela nos permite entender se o modelo está se beneficiando de mais dados de treinamento ou se está atingindo seu limite de desempenho.
           - Se a curva de aprendizado mostrar que o desempenho do modelo continua a melhorar à medida que mais dados são adicionados, isso sugere que o modelo se beneficiaria de mais dados de treinamento.
           - Se a curva de aprendizado mostrar que o desempenho do modelo estabiliza ou mesmo piora à medida que mais dados são adicionados, isso sugere que o modelo atingiu seu limite de desempenho e que adicionar mais dados pode não ser útil.
        """
        st.markdown(info_describe)
        info_describe = """
          Em resumo, a proximidade das curvas de aprendizado na base de treinamento e na base de validação sugere que o modelo está aprendendo bem com os dados de treinamento e generalizando efetivamente para novos dados, sem evidências claras de sobreajuste. Isso é geralmente considerado um resultado positivo.
        """
 
        setTextImagem(info_describe,"learning_curve.png", 'Curva de Aprendizado' )
        
        info_describe = """
          Uma curva de validação com pontuação de 0,6 na base de validação sugere um problema de overfitting.
          - Para melhorar esse resultado, algumas abordagens podem ser consideradas:
          - Regularização: Se você estiver usando modelos como regressão linear ou árvores de decisão, pode considerar a aplicação de técnicas de regularização para controlar o overfitting.
          - Redução da Complexidade do Modelo: Reduza a complexidade do modelo, por exemplo, reduzindo o número de recursos ou a profundidade das árvores de decisão, para tornar o modelo mais genérico e menos propenso a se ajustar demais aos dados de treinamento.
          - Aumentar o Tamanho do Conjunto de Dados de Treinamento: Se possível, adquira mais dados de treinamento para que o modelo possa aprender com uma variedade maior de exemplos e padrões.
          - Seleção de Características: Selecione apenas as características mais importantes e relevantes para o problema em questão, eliminando características irrelevantes ou redundantes que possam estar contribuindo para o overfitting.

        """
        st.markdown(info_describe)
        
        info_describe = """
          Em resumo, a proximidade das curvas de aprendizado na base de treinamento e na base de validação sugere que o 
          modelo está aprendendo bem com os dados de treinamento e generalizando efetivamente para novos dados, sem evidências claras de sobreajuste. 
          Isso é geralmente considerado um resultado positivo.
        """

        setTextImagem(info_describe,"validation_curve.png", 'Curva de Validação' )
        
        
        info_describe = """
          A matriz de confusão é uma ferramenta que mostra a performance de um modelo de classificação.
          Na primeira linha da matriz:
          - O modelo previu corretamente 1382 instâncias da classe negativa (True Negative - TN), ou seja, quando a previsão foi "Não Cesta" e a verdade é "Não Cesta".
          - O modelo previu incorretamente 737 instâncias da classe positiva (False Positive - FP), ou seja, quando a previsão foi "Não Cesta" mas a verdade é "Cesta".
          Na segunda linha da matriz:
          - O modelo previu incorretamente 974 instâncias da classe negativa (False Negative - FN), ou seja, quando a previsão foi "Cesta" mas a verdade é "Não Cesta".
          - O modelo previu corretamente 963 instâncias da classe positiva (True Positive - TP), ou seja, quando a previsão foi "Cesta" e a verdade é "Cesta".

        """
  
        setTextImagem(info_describe,"confusion_matrix_lr.png", 'Matriz de Confusão - Logistic Regression' )
        
        info_describe = """
          Matriz de Confusão - RandomForestClassifier
          Na primeira linha da matriz:
          - O modelo previu corretamente 1221 instâncias da classe negativa (True Negative - TN), ou seja, quando a previsão foi "Não Cesta" e a verdade é "Não Cesta".
          - O modelo previu incorretamente 889 instâncias da classe positiva (False Positive - FP), ou seja, quando a previsão foi "Não Cesta" mas a verdade é "Cesta".
          Na segunda linha da matriz:
          - O modelo previu incorretamente 892 instâncias da classe negativa (False Negative - FN), ou seja, quando a previsão foi "Cesta" mas a verdade é "Não Cesta".
          - O modelo previu corretamente 1045 instâncias da classe positiva (True Positive - TP), ou seja, quando a previsão foi "Cesta" e a verdade é "Cesta".

        """ 
        setTextImagem(info_describe, "confusion_matrix_rf.png", 'Matriz de Confusão - RandomForestClassifier' )
        
        info_describe = """
         No geral, um valor próximo de 0.6 indica que o modelo está tendo um desempenho moderado, mas ainda há espaço para melhorias. Dependendo do contexto do problema e dos requisitos específicos, pode ser necessário ajustar o modelo, considerar diferentes algoritmos ou explorar mais os dados para melhorar o desempenho do modelo
       
        """ 
        setTextImagem(info_describe, "classification_report_lr.png", 'Classification Report Regreção Logistica' ) 
        
        info_describe = """
         Quando a precisão, recall e F1-score ficam próximos de 0.55, isso indica que o modelo está tendo um desempenho moderado, mas pode ser aprimorado. Vamos interpretar cada métrica:
         - Precisão (Precision): A precisão representa a proporção de exemplos classificados como positivos que são realmente positivos. Uma precisão de cerca de 0.55 significa que aproximadamente 55% dos exemplos classificados como positivos são realmente positivos. Em outras palavras, das previsões de "Cesta", cerca de 55% são corretas.
         - Revocação (Recall): A revocação (também conhecida como sensibilidade) representa a proporção de exemplos positivos que foram corretamente identificados pelo modelo. Aqui, cerca de 55% dos exemplos positivos foram corretamente identificados pelo modelo. Isso significa que o modelo está capturando aproximadamente 55% dos exemplos verdadeiros de "Cesta".
         - F1 Score: O F1-score é a média harmônica entre precisão e revocação. Ele fornece um equilíbrio entre essas duas métricas. Um F1-score de cerca de 0.55 indica um equilíbrio razoável entre a capacidade do modelo de fazer previsões corretas (precisão) e de capturar exemplos positivos (revocação).

        """ 
        setTextImagem(info_describe, "classification_report_rf.png", 'Classification Report  RandomForestClassifier' ) 
        
        info_describe = """
           Em geral, uma AUC entre 0,5 e 0,7 é considerada aceitável, mas ainda há margem para melhorias no desempenho do modelo. Uma AUC maior que 0,7 é geralmente considerada boa, enquanto valores próximos de 1 indicam um excelente desempenho na classificação.
        """ 
        setTextImagem(info_describe, "roc_curve.png", 'Curva ROC' ) 
        
        st.subheader("Notebook Treinamento")
        notebook_url = "https://raw.githubusercontent.com/wolfxweb/eng_machine_learning/main/code/Treinamento.ipynb"
        exibir_codigo_notebook(notebook_url) 
        
        
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
