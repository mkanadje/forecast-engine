import streamlit as st
import pandas as pd
import requests

st.title("Forecast Engine Test App")

api_url = "http://localhost:8000/forecast"

uploaded_file = st.file_uploader(
    "Upload CSV file with a single column time series data", type=["csv"]
)
steps = st.number_input("Number of steps to forecast", min_value=1, value=5)
model = st.selectbox("Select forecasting model", ["arima"])

data_list = []

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=None)
    if df.shape[1] != 1:
        st.error("CSV file must contain a single column of time series data.")
    else:
        st.write("Data Preview:", df.head())
        data_list = df.iloc[:, 0].tolist()

if st.button("Run Forecast"):
    if not data_list:
        st.error("Please upload a valid CSV file with time series data.")
    else:
        payload = {
            "data": data_list,
            "steps": steps,
            "model": model,
        }
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Forecast: {result['forecast']}")
            st.write(f"Model used: {result['model_used']}")
        else:
            st.error(f"Error: {response.text}")
