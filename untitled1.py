# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nS_BXyU-dOd1KYzVncCLVBwrrwiRLBMX
"""



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Title
st.title("Vata, Pitta, Kapha Pulse Monitoring")

# File selection
file_option = st.selectbox("Choose dataset", ["Right Hand (R_V_P_K)", "Left Hand (S_V_P_K)"])

# Load selected file
file_path = "R_V_P_K.xlsx" if file_option == "Right Hand (R_V_P_K)" else "S_V_P_K.xlsx"
df = pd.read_excel(file_path)

# Show raw data
st.subheader("Raw Data")
st.dataframe(df.head())

# Extract columns
time = df.iloc[:, 0]
vata = df.iloc[:, 1]
pitha = df.iloc[:, 2]
kapha = df.iloc[:, 3]

# Apply Savitzky-Golay filter to smooth the signals (noise removal)
vata_smooth = savgol_filter(vata, window_length=11, polyorder=3)
pitha_smooth = savgol_filter(pitha, window_length=11, polyorder=3)
kapha_smooth = savgol_filter(kapha, window_length=11, polyorder=3)

# Plotting
st.subheader("Smoothed Pulse Signals")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(time, vata_smooth, label="Vata", color="blue")
ax.plot(time, pitha_smooth, label="Pitha", color="orange")
ax.plot(time, kapha_smooth, label="Kapha", color="green")
ax.set_xlabel("Time")
ax.set_ylabel("Pulse Amplitude")
ax.set_title("Pulse Signals of Vata, Pitha, Kapha")
ax.legend()
st.pyplot(fig)