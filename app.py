import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Stremlit Demo ")
st.subheader("by Y.F.")

df = px.data.iris()

st.write(df)

st.write(px.scatter(df, x="sepal_length", y="sepal_width", color="species"))
             
        