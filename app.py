import streamlit as st
import pandas as pd

st.title("📊 Data Visualisation Helper")
st.write("Upload a CSV or Excel file to get column type detection, X/Y suggestions, duplicate detection, and aggregation.")



# --- Data Aggregation ---
st.write("### Data Aggregation")

# Select grouping column (categorical/object)
group_col = st.selectbox(
    "Select a column to group by (categorical/object)",
    options=[col for col in df.columns if pd.api.types.is_object_dtype(df[col])]
)

# Select aggregation function
agg_func = st.selectbox(
    "Select aggregation function for numeric columns",
    options=["sum", "mean", "median", "min", "max", "count"]
)

if group_col:
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        aggregated = df.groupby(group_col)[numeric_cols].agg(agg_func)
        st.write(f"### Aggregated data by `{group_col}` using `{agg_func}`")
        st.dataframe(aggregated)
    else:
        st.write("No numeric columns to aggregate.")








