import pandas as pd
import streamlit as st
import datetime

titanic_link = "https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/titanic.csv"

titanic_data = pd.read_csv(titanic_link)

#create the title for the web app
st.title("My firts Streamlit App")
sidebar = st.sidebar
sidebar.title("This is the sidebar")
sidebar.write("You can add any elements to thr sidebar.")

#Give user the courrent date

today =datetime.date.today()
today_date = st.date_input('Courrent date ', today)

st.success('Current sate : ´%s´ ' % (today_date))

# Display the content of the dataset if checkbox is true

st.header("Dataset")
agree = sidebar.checkbox("Show Dataset Overview ? ")
if agree:
    st.dataframe(titanic_data)

# Select the embark town of the passanger and the display the dataset with this selections
selected_town = sidebar.radio("Select Embark Town", titanic_data['embark_town'].unique())
st.write("Select Embark Town:", selected_town)

st.write(titanic_data.query(f"""embark_town==@selected_town"""))

st.markdown("_______")

#Select arange of the farce and the display the dataset with this selection
optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimun Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Miximun Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)

subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of records with Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

# Display of the dataset
st.dataframe(subset_fare)