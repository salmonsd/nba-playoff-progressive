import streamlit as st
import pandas as pd

data = pd.read_csv("2022_playoff_progressive.csv",parse_dates=True)
data.Date = data.Date = pd.to_datetime(data.Date)
data = data.set_index("Date")

st.title("2022 Playoff Progressive")

st.subheader("Graph")
st.line_chart(data)

st.subheader("Data")
st.dataframe(data)

