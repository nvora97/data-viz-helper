import streamlit as st
import pandas as pd

st.title("📊 Data Visualisation Helper")
st.write("Upload a CSV or Excel file and get suggestions for X/Y columns and chart types!")

# File upload
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Preview of your data")
    st.dataframe(df.head())

    # Detect column types
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    date_cols = df.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()

    # Suggest X/Y combinations
    st.write("### Suggested X/Y column pairs and chart types")
    suggestions = []

    for x_col in df.columns:
        for y_col in numeric_cols:  # Y-axis must be numeric
            if x_col == y_col:
                continue  # skip same column
            # Determine chart type
            if x_col in date_cols:
                chart_type = "Line / Area chart (Time Series)"
            elif x_col in categorical_cols:
                chart_type = "Bar chart / Column chart"
            elif x_col in numeric_cols:
                chart_type = "Scatter plot"
            else:
                chart_type = "Other / Custom"
            suggestions.append((x_col, y_col, chart_type))

    # Display suggestions in table
    if suggestions:
        suggestion_df = pd.DataFrame(suggestions, columns=["X-axis", "Y-axis", "Suggested Chart"])
        st.dataframe(suggestion_df)
    else:
        st.write("No valid column pairs found for suggestions.")

