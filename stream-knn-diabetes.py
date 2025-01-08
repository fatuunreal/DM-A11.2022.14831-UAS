import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('knn_diabetes_model.sav', 'rb'))

#judul web
st.title('Prediksi Diabetes Dengan KNN')

#membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')

with col2:
    Glucose = st.text_input('Input nilai Glucose')

with col1:
    BloodPressure = st.text_input('Input nilai Blood Pressure')

with col2:
    SkinThickness = st.text_input('Input nilai Skin Thickness')

with col1:
    Insulin = st.text_input('Input nilai Insulin')

with col2:
    BMI = st.text_input('Input nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
    Age = st.text_input('Input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        # Konversi input ke tipe numerik
        Pregnancies = int(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = int(Age)

        # Prediksi
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'
        st.success(diab_diagnosis)

    except ValueError:
        st.error("Harap masukkan nilai numerik yang valid.")
