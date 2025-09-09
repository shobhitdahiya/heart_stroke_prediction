

# 🫀 Heart Stroke Risk Prediction

This project is a **Machine Learning-based web application** that predicts the risk of a heart stroke based on medical and lifestyle data.
The aim is to assist in **early risk identification** and provide better decision-making support for healthcare professionals.

🔗 **Live Demo**: [Heart Stroke Prediction App](https://heartstrokeprediction-p3xbqu68g7zylwkvcvyveu.streamlit.app/)

---

## 🚀 Features

* Predicts stroke risk using medical and lifestyle attributes.
* Clean and user-friendly **Streamlit web interface**.
* Scalable and easy-to-deploy ML pipeline.
* Supports real-time predictions after user input.

---

## 🛠️ Tech Stack

* **Python** (scikit-learn, pandas, numpy)
* **Machine Learning Models** (SVM, Logistic Regression)
* **Streamlit** for deployment and frontend
* **Pickle** for model persistence

---

## 📂 Project Structure

```
├── app.py              # Streamlit app script
├── heart.py            # Helper functions for predictions
├── Columns.pkl         # Feature columns
├── SVM_heart.pkl       # Trained ML model
├── Scaler.pkl          # Standard scaler object
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚡ How to Run Locally

1. Clone this repo:

   ```bash
   git clone https://github.com/shobhitdahiya/heart_stroke_prediction.git
   cd heart_stroke_prediction
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit app:

   ```bash
   streamlit run app.py
   ```
4. Open the local URL (shown in terminal) to access the app.

---

## 📊 Dataset

The dataset used contains attributes like:

* Age, Gender, BMI
* Hypertension, Heart Disease
* Average Glucose Level, Smoking Status, etc.

---

## 🎯 Future Improvements

* Add more advanced models (XGBoost, Random Forest).
* Deploy with Docker for scalability.
* Add visual analytics dashboard.

---

## 👨‍💻 Author

**Shobhit Raj Dahiya**

* 💼 [LinkedIn](https://www.linkedin.com/in/shobhitrajdahiya/)
* 📂 [GitHub](https://github.com/shobhitdahiya)

---


