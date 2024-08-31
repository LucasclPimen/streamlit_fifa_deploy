import streamlit as st
import pandas as pd

st.set_page_config(

    page_title = 'Teams',
    page_icon = '⚽', 
    layout = 'wide',
)

df_data = st.session_state['data']

teams = df_data['Club'].value_counts().index
team = st.sidebar.selectbox('Time', teams)

df_team = df_data[df_data['Club'] == team].set_index('Name')

st.image(df_team['Club Logo'].iloc[0])  # Aparece mais de uma vez, então, iloc[0] usa somente a primeira aparição
st.markdown(f"## {team}")

columns = ['Age','Photo','Flag','Overall','Value(£)','Wage(£)','Joined','Height','Weight','Contract Valid Until','Release Clause(£)']

st.dataframe(df_team[columns],
             column_config= {
                 "Overall": st.column_config.ProgressColumn(
                    'Overall', format = "%d", min_value=0, max_value = 100  # "%d" = formatação de inteiro
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                    "Weekly Wage", format = '£%f', min_value=0, max_value = df_team['Wage(£)'].max()
                 ),
                 "Photo":st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn('Country')
             }
             )

