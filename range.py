import streamlit as st
import pandas as pd

st.title( 'Streamlit - Search ranges')

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/calculadora-4c7ba.appspot.com/o/datasets%2Fdataset.csv?alt=media&token=f9b7648c-91e6-44dd-ac67-49c7e531d611')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data[ (data['index'] >= startid) & (data['index'] <= endid) ]

    return filtered_data_byrange

startid = st.text_input('Start index :')
endid = st.text_input('End index :')
btnRange = st.button( 'Search by range')

if (btnRange):
    filterbyrange = load_data_byrange(int (startid), int(endid))
    count_row = filterbyrange.shape[0] # Gives number of rows
    st.write (f"Total items : {count_row}")
    
    st.dataframe(filterbyrange)