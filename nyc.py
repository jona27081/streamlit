import streamlit as st
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')
st.header("Jonathan Arath Ojeda Rosas")
st.markdown("ZS20006736@ESTUDIANTES.UV.MX")

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text("Hecho! (using st.cache)")

st.sidebar.image("Credencial.jpeg")
st.sidebar.markdown("##")

if st.sidebar.checkbox('Ver datos sin procesar'):
    st.subheader('Datos sin procesar ')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora '):
    st.subheader('Numero de recorridos por hora: ')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


# Some number in the range 0-23
hour_to_filter = st.sidebar.slider('Hora', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)