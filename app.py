import streamlit as st
import pandas as pd

st.title("📊 Data Helper Tool")
st.write(
    "Upload a CSV or Excel file to get column type detection, X/Y suggestions, duplicate detection, and aggregation."
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
    columns_to_check = st.multiselect("Chec









