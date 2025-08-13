import streamlit as st
import pandas as pd
import joblib

# --- Load saved model, scaler, and expected columns ---
model = joblib.load("SVM_heart.pkl")
scaler = joblib.load("Scaler.pkl")
expected_columns = joblib.load("Columns.pkl")

# --- Page Config ---
st.set_page_config(page_title="Heart Stroke Risk Predictor ❤️", page_icon="❤️", layout="centered")

# --- Title & Description ---
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>❤️ Heart Stroke Risk Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Fill the details below and find out your heart stroke risk instantly.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Create Input Form ---
with st.form("heart_form"):
    st.subheader("📋 Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 18, 100, 40)
        sex = st.selectbox("Sex", ["M", "F"])
        chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    with col2:
        resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
        cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])

    st.subheader("🫀 Heart & Exercise Details")
    col3, col4 = st.columns(2)
    with col3:
        resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
        max_hr = st.slider("Max Heart Rate", 60, 220, 150)
        exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    with col4:
        oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0, step=0.1)
        st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    # --- Submit Button ---
    submitted = st.form_submit_button("🔍 Predict Risk")

# --- Prediction Logic ---
if submitted:
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ **High Risk of Heart Disease!**\n\nPlease consult a doctor immediately and take preventive measures.")
    else:
        st.success("✅ **Low Risk of Heart Disease**\n\nKeep up a healthy lifestyle! 💪")

    # Optional: Show user input table
    with st.expander("📊 View Your Input Data"):
        st.dataframe(input_df)
