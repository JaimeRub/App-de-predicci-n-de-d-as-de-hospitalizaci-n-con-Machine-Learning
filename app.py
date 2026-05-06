import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load('modelo_random_forest.pkl')

st.title("Predicción de días de hospitalización")

edad = st.number_input("Edad", 0, 120, 30)
sexo_m = st.selectbox("Sexo masculino", ["No", "Sí"])

if st.button("Predecir"):

    data = {
        'edad_anios': edad,
        'ViaIngreso_3': False,

        'CausaExterna_12': False,
        'CausaExterna_13': True,
        'CausaExterna_15': False,

        'TipoUsuario_2': False,
        'TipoUsuario_3': False,
        'TipoUsuario_4': False,

        'Sexo_M': True if sexo_m == "Sí" else False,

        'grupo_cie10_Circulatorio': False,
        'grupo_cie10_Congénitas': False,
        'grupo_cie10_Embarazo': False,
        'grupo_cie10_Infecciosas y parasitarias': False,
        'grupo_cie10_Mentales': False,
        'grupo_cie10_Musculoesquelético': False,
        'grupo_cie10_Respiratorio': True,
        'grupo_cie10_Sentidos (ojo/oído)': False,
        'grupo_cie10_Tumores': False
    }

    df = pd.DataFrame([data])

    pred = modelo.predict(df)

    st.write("Días estimados:", pred[0])