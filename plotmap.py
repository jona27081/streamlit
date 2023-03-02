import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [18.894324, -96.790051],
    columns=['lat', 'lon'])

st.map(map_data)