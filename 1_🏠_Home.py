import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

#if 'data' not in st.session_state: # Se não houver 'data', executar função
    #df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col = 0)
    #df_data['Contract Valid Until'] = df_data['Contract Valid Until'].apply(lambda x: int(x))
    #df_data = df_data[df_data['Contract Valid Until']>=datetime.today().year]
    #df_data = df_data[df_data['Value(£)'] > 0]
    #df_data.sort_values(by = 'Overall', ascending= False, inplace = True)
    #st.session_state['data'] = df_data
st.set_page_config(
    page_title='Home',
    page_icon = '🏠',
    layout = 'wide'
)
@st.cache_data
def load_data():
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col = 0)
    df_data['Contract Valid Until'] = df_data['Contract Valid Until'].apply(lambda x: int(x))
    df_data = df_data[df_data['Contract Valid Until']>=datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data.rename(columns= {'Height(cm.)':'Height', 'Weight(lbs.)':'Weight'}, inplace = True)
    df_data['Height'] = df_data['Height'].apply(lambda x: float(x/100))
    df_data.sort_values(by = 'Overall', ascending= False, inplace = True)
    return df_data

df_data = load_data()

st.session_state['data'] = df_data


st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")

st.sidebar.markdown('Desenvolvido por [Lucas Pimentel](https://www.linkedin.com/in/lucas-cl-pimentel/)') # coloca links no que está entre colchetes

btn = st.link_button('Acesse os dados no Kaggle','https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')


st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)


