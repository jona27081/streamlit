import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('uber_dataset.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

# Some number in the range 0-23
day_to_filter = st.slider('Day', 0, 1, 30)
filtered_data = data[data[DATE_COLUMN].dt.day == day_to_filter]

st.subheader('Map of all pickups day %s' % day_to_filter)
st.map(filtered_data)
