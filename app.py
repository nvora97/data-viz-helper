import streamlit as st
import pandas as pd

st.title("📊 Data Visualisation Helper - X/Y Suggestions Only")
st.write("Upload a CSV or Excel file to get suggested X/Y column pairs based on types.")

# File upload
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load the file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, parse_dates=True, dayfirst=True, infer_datetime_format=True)
        else:
            df = pd.read_excel(uploaded_file, parse_dates=True)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    # Preview data
    st.write("### Preview of your data")
    st.dataframe(df.head())

    # Detect column types
    st.write("### Column Types Detected")
    st.write(df.dtypes)

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    date_cols = df.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()

    # Suggest X/Y combinations
    st.write("### Suggested X/Y column pairs")
    suggestions = []

    for x_col in df.columns:
        for y_col in df.columns:
            if x_col == y_col:
                continue

            x_dtype = df[x_col].dtype
            y_dtype = df[y_col].dtype
            suggested_chart = None

            # Numeric Y-axis
            if pd.api.types.is_numeric_dtype(y_dtype):
                if pd.api.types.is_datetime64_dtype(x_dtype):
                    suggested_chart = "Line / Area chart (Time Series)"
                elif pd.api.types.is_categorical_dtype(x_dtype):
                    suggested_chart = "Bar chart / Column chart"
                elif pd.api.types.is_numeric_dtype(x_dtype):
                    suggested_chart = "Scatter plot"
            # Categorical Y-axis + Categorical X-axis
            elif pd.api.types.is_categorical_dtype(y_dtype) and pd.api.types.is_categorical_dtype(x_dtype):
                suggested_chart = "Grouped Bar / Heatmap"

            if suggested_chart:
                suggestions.append((x_col, y_col, suggested_chart))

    if suggestions:
        suggestion_df = pd.DataFrame(suggestions, columns=["X-axis", "Y-axis", "Suggested Chart"])
        st.dataframe(suggestion_df)
    else:
        st.write("No valid column pairs found. Check your data types or clean missing values.")




