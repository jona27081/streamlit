import streamlit as st
import pandas as pd

st.title('Mangas')

DATA_URL = ('Mangas.csv')

@st.cache
def load_data(name):
    data = pd.read_csv(DATA_URL)
    data['Name'] = data['Name'].fillna('')
    data['Name'] = data['Name'].str.upper()
    filtered_data_byname = data[data['Name'].str.contains(name) ]

    return data

myname = st.text_input( 'Titulo:')
myname =  myname.upper()

if (myname):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0] # Gives number of rows
    st.write(f"Total nombres: {count_row}")

    st.dataframe (filterbyname)
