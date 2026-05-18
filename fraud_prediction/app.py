import streamlit as st
import pandas as pd
import joblib

# tampilan app
st.set_page_config(page_title="ML Fraud Detection", page_icon="", layout="wide")

# Membuat Judul
st.title("Fraud Detection app")
st.write("This app running with Machine Learning (Random Forest) to analyze digital footprints and predict suspicious transactions in real-time.")
st.write("Enter transactions in the left sidebar for analysis.")

st.divider()

try:
    model = joblib.load('deteksi_fraud.pkl')
    st.success("Model loaded successfully!")
except FileNotFoundError:
    st.error("File not found, please try again")

#import file
df_raw = pd.read_csv('banking_transactions.csv')
X_raw = df_raw.drop(columns=['transaction_id', 'fraud_flag'])
#template 1 baris berisi nilai rata-rata dari semua data
X_template = pd.get_dummies(X_raw, drop_first=True).mean().to_dict()

#UI SIDEBAR
st.sidebar.header("Transaction Input")
st.sidebar.write("Mausukan jejak transaksi di bawah ini:")

#slider dan input angka
input_anomaly = st.sidebar.slider("Anomaly Score", min_value=0.0, max_value=1.0, value=0.69, step=0.01)
input_geo = st.sidebar.number_input("Geographical Distance (km)", min_value=0.0, value=15.0)
input_balance = st.sidebar.number_input("Avg Monthly Balance ($)", min_value=0.0, value=70000.0)
input_amount = st.sidebar.number_input("Transaction Amount ($)", min_value=0.0, value=70000.0)


#Model prediksi
if st.sidebar.button("Detect Fraud"):

    #nilai rata-rata
    user_data = X_template.copy()

    #nilai default dengan inputan user
    user_data['anomaly_score'] = input_anomaly
    user_data['geo_distance_km'] = input_geo
    user_data['avg_monthly_balance'] = input_balance
    user_data['transaction_amount'] = input_amount

    # Ubah format dictionary menjadi DataFrame agar bisa dibaca model
    df_user = pd.DataFrame([user_data])

    # model melakukan tebakan
    hasil_prediksi = model.predict(df_user)
    probabilitas = model.predict_proba(df_user)[0]

    #hasil
    st.subheader("Model Analysis Result:")

    #visual
    persentase_fraud = probabilitas[1] * 100
    st.write(f"Model presentase : **{persentase_fraud:.2f}%** indications of fraud.")

    st.progress(probabilitas[1])


    if hasil_prediksi[0] == 1:
        st.error("⚠️HIGH RISK! This transaction exhibits strong indicators of fraud. Action required immediately.")
    else:
        st.success("The digital footprints of this transaction appear normal.")
