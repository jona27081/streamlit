import streamlit as st

#titulo del content
st.title("App con sidebar")

sidebar = st.sidebar

sidebar.title("Esta es el sidebar")
sidebar.write("Datos del sidebar")

st.header("Header 1")
st.header("Header 2")
st.write("Datos del content")