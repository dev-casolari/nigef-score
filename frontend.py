import streamlit as st

from utils import calculate_score

col1, col2, col3, col4, col5, col6 = st.columns([0.15, 0.14, 0.14, 0.17, 0.15, 0.3])


sex = col1.radio("SESSO", ["uomo", "donna"])
age = col2.radio("ETA" , ["0-20", "21-35", "36-50", "51+"])
bmi = col3.radio("BMI", ["<18", "18-25", "25-30", "30-35", "35-40", "40+"])
activity = col4.radio("TIPO ATTIVITA", ["leggera", "media", "pesante"])
sport = col5.radio("ORE SPORT", ["0", "1-3", "4-6", "7+"])
objective = col6.radio("OBIETTIVO" , ["mantenimento", "dimagrimento", "aumento"])

if st.button("CALCOLA PUNTEGGIO"):
  score = calculate_score(sex, age, bmi, activity, sport, objective)
  st.write("Punteggio: ", score)