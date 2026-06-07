import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("Placement Predictor")

cgpa = st.number_input("Enter CGPA")
iq = st.number_input("Enter IQ")

if st.button("Predict"):

    prediction = model.predict([[cgpa, iq]])

    if prediction[0] == 1:
        st.success("Student will be Placed")
    else:
        st.error("Student will NOT be Placed")