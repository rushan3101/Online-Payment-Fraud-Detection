import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("fraud_detection_model.pkl")

st.title("💳 Online Payment Fraud Detection")

st.write("Enter transaction details:")

# User Inputs
payment_type = st.selectbox(
    "Payment Type",
    ["TRANSFER", "CASH_OUT", "CASH_IN", "PAYMENT", "DEBIT"]
)

amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Sender Old Balance", min_value=0.0)
newbalanceOrig = st.number_input("Sender New Balance", min_value=0.0)
oldbalanceDest = st.number_input("Receiver Old Balance", min_value=0.0)
newbalanceDest = st.number_input("Receiver New Balance", min_value=0.0)

if st.button("Predict Fraud"):

    input_df = pd.DataFrame([{
        "type": payment_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prob = model.predict_proba(input_df)[0][1]

    threshold = 0.991

    if prob >= threshold:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
