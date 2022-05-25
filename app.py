import streamlit as st
import pandas as pd
import plotly.express as px

# Running Totals
data = pd.read_csv("2022_playoff_progressive.csv", parse_dates=True)
data.Date = data.Date = pd.to_datetime(data.Date)
data = data.set_index("Date")

# Daily Picks
daily_picks_df = pd.read_csv("2022_playoff_picks.csv", parse_dates=True)
daily_picks_df.Date = pd.to_datetime(daily_picks_df.Date)
daily_picks_df = daily_picks_df.set_index("Date")

st.title("2022 Playoff Progressive")

st.subheader("Graph")
fig = px.line(data, title="Total Points over Time")
st.plotly_chart(fig)

st.subheader("Stat Analysis")
st.table(daily_picks_df.describe())

st.subheader("Data")
st.dataframe(data)
