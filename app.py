import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Plotly Test")

df = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Value": [10, 20, 15]
})

fig = px.bar(df, x="Category", y="Value", title="Test Chart")
st.plotly_chart(fig)




