import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Players',
    page_icon = '🏃‍♂️',
    layout="wide",
    )

df_data = st.session_state['data']
clubes = df_data['Club'].value_counts().index
clube = st.sidebar.selectbox('Clube',clubes)

df_clube = df_data[df_data['Club'] == clube]

players = df_clube['Name'].value_counts().index

player = st.sidebar.selectbox('Jogador', players)

df_player = df_clube[df_clube['Name'] == player].iloc[0] # filtro para manipulação com os elementos associados ao jogador

st.image(df_player['Photo'])
st.title(df_player['Name'])

st.markdown(f"**Clube**: {df_player['Club']}")
st.markdown(f"**Posição**: {df_player['Position']}")

col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25])

col1.markdown(f"**Idade**: {df_player['Age']}")
col2.markdown(f"**Altura (m)**: {df_player['Height']}")
col3.markdown(f"**Peso (lbs)**: {np.round(df_player['Weight'],2)}")
 
st.divider() # Análogo ao html.Hr() - quebra de linha no layout

st.subheader(f"Overall: {df_player['Overall']}")
st.progress(int(df_player['Overall']))

col1,col2, col3, col4 = st.columns(4)
col1.metric('Valor de Mercado', value= f"£ {df_player['Value(£)']:,}")
col2.metric('Remuneração Semanal', value = f"£ {df_player['Wage(£)']:,}")
col3.metric('Valor de Recisão', value = f"£ {df_player['Release Clause(£)']:,}")










