import streamlit as st
import pandas as pd

st.title( 'Mangas')
DATA_URL = ('Mangas.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

@st.cache
def load_data_bysex(status):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data['status' ] == status]
    
    return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select Sex", data['status'].unique())
btnFilterbySex = st.button('Filter by status')

if (btnFilterbySex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0] # Gives number of rows
    st.write(f"Total items : {count_row}")

    st.dataframe (filterbysex)