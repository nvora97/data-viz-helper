import streamlit as st
import pandas as pd

st.title("📊 Data Visualisation Helper")

st.write("Upload a CSV or Excel file and I'll suggest visualisations based on your columns!")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Preview of your data")
    st.dataframe(df.head())

    # Suggest visualisations
    st.write("### Suggested Visualisations")

    for col in df.columns:
        dtype = df[col].dtype
        
        if dtype == "object":
            st.write(f"🟦 **{col}** → Bar Chart, Pie Chart")
        elif pd.api.types.is_numeric_dtype(dtype):
            st.write(f"🟥 **{col}** → Line Chart, Histogram, Scatter Plot")
        else:
            st.write(f"⬜ **{col}** → Other/Custom Visualisation")
