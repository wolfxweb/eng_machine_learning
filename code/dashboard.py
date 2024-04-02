import streamlit as st
import pandas as pd
import pickle

# Função para carregar o modelo
@st.cache
def load_model():
    with open('best_model_RandomForestClassifier.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Função para fazer previsões com o modelo carregado
def fazer_previsao(model, input_data):
    # Verificar se a coluna 'shot_distance' está presente no conjunto de dados
    if 'shot_distance' in input_data.columns:
        # Remover a coluna 'shot_distance' do conjunto de dados
        input_data = input_data.drop(columns=['shot_distance'])
    # Faça a previsão com o modelo
    resultado = model.predict(input_data)
    return resultado

# Carregar o modelo
model = load_model()

# Interface do usuário
st.title('Aplicativo de Modelo')
st.write('Este aplicativo carrega um modelo treinado e faz previsões com base nos dados inseridos.')

# Carregar os dados de entrada
input_data = pd.read_parquet('../data/raw/dataset_kobe_prod.parquet')

# Botão para fazer a previsão
if st.button('Fazer Previsão'):
    # Faça a previsão com os dados inseridos
    resultado = fazer_previsao(model, input_data)
    # Exibir o resultado da previsão
    st.write('O resultado da previsão é:', resultado)
