import streamlit as st
import pandas as pd

st.title("📊 Data Analysis Helper - Statistics & X/Y Suggestions")
st.write("Upload a CSV or Excel file to analyze your dataset with statistics, correlations, and suggestions.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # --- Load File ---
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, parse_dates=True, dayfirst=True, infer_datetime_format=True)
        else:
            df = pd.read_excel(uploaded_file, parse_dates=True)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    st.write("### Preview of your data")
    st.dataframe(df.head())

    # --- Column Types ---
    st.write("### Column Types Detected")
    st.write(df.dtypes)

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    date_cols = df.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()

    # --- Descriptive Statistics ---
    st.write("### Descriptive Statistics")
    if numeric_cols:
        st.write("**Numeric Columns**")
        st.da




