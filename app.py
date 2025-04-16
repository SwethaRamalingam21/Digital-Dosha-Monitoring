# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B19Z6TaapdjXudrVbLBHkAOKnYLbLsv3
"""

!pip install streamlit

# app.py

import streamlit as st
import pandas as pd
import zipfile
import os
import plotly.express as px

st.set_page_config(page_title="Digital Dosha Monitoring", layout="wide")
st.title("🌿 Digital Dosha Monitoring Dashboard")

uploaded_file = st.file_uploader("Upload Sensor Data (ZIP file)", type="zip")

if uploaded_file is not None:
    zip_path = os.path.join("temp_data.zip")

    with open(zip_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("unzipped_data")

    # Automatically load the first CSV inside the extracted folder
    csv_files = [file for file in os.listdir("unzipped_data") if file.endswith(".csv")]

    if csv_files:
        df = pd.read_csv(os.path.join("unzipped_data", csv_files[0]))
        st.success(f"Loaded file: {csv_files[0]}")

        st.subheader("📊 Raw Data Preview")
        st.dataframe(df.head())

        st.subheader("📈 Feature Visualizations")

        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if numeric_cols:
            selected_feature = st.selectbox("Select feature to visualize", numeric_cols)
            fig = px.line(df, y=selected_feature, title=f"{selected_feature} Over Time")
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📌 Summary Statistics")
            st.write(df[numeric_cols].describe())

        else:
            st.warning("No numeric columns found for visualization.")

    else:
        st.error("No CSV files found in the ZIP archive.")