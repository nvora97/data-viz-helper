import streamlit as st
import pandas as pd

st.title("📊 Data Visualisation Helper")
st.write(
    "Upload a CSV or Excel file to get column type detection, X/Y suggestions, and duplicate detection."
)

# --- File Upload ---
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # --- Load File ---
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    # --- Preview Data ---
    st.write("### Preview of your data")
    st.dataframe(df.head())

    # --- Column Types ---
    st.write("### Column Types Detected")
    st.write(df.dtypes)

    # --- Duplicate Detection ---
    st.write("### Duplicate Detection")

    # Full row duplicates
    duplicate_rows = df[df.duplicated()]
    st.write(f"Duplicate Rows (exact match across all columns): {len(duplicate_rows)}")
    if not duplicate_rows.empty:
        st.dataframe(duplicate_rows)

    # Optional: duplicates by selected columns
    columns_to_check = st.multiselect("Check duplicates in specific columns", df.columns)
    if columns_to_check:
        duplicates = df[df.duplicated(subset=columns_to_check)]
        st.write(f"Duplicate Rows based on selected columns: {len(duplicates)}")
        if not duplicates.empty:
            st.dataframe(duplicates)

    # --- Suggested X/Y pairs with categorical → X, numeric → Y ---
    st.write("### Suggested X/Y Column Pairs")
    suggestions = []
    for x_col in df.columns:
        for y_col in df.columns:
            if x_col == y_col:
                continue

            x_dtype = df[x_col].dtype
            y_dtype = df[y_col].dtype
            suggested_chart = None

            # Enforce categorical/object → X-axis, numeric → Y-axis
            if pd.api.types.is_numeric_dtype(y_dtype) and pd.api.types.is_object_dtype(x_dtype):
                suggested_chart = "Bar / Column Chart"
            elif pd.api.types.is_numeric_dtype(x_dtype) and pd.api.types.is_numeric_dtype(y_dtype):
                suggested_chart = "Scatter Plot"
            elif pd.api.types.is_object_dtype(x_dtype) and pd.api.types.is_object_dtype(y_dtype):
                suggested_chart = "Grouped Bar / Heatmap"

            if suggested_chart:
                suggestions.append((x_col, y_col, suggested_chart))

    if suggestions:
        suggestion_df = pd.DataFrame(suggestions, columns=["X-axis", "Y-axis", "Suggested Chart"])
        st.dataframe(suggestion_df)
    else:
        st.write("No valid column pairs found.")








