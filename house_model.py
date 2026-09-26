import streamlit as st
import joblib

app = joblib.load("models/MyAi.pkl")

st.title("HOUSE PRICE PREDICTION")

#"Area_sqft","Bedrooms","Bathrooms"
area_sqft = st.number_input("Area SQFT:")
bedroom = st.number_input("Bedrooms:")
bathroom = st.number_input("Bathrooms:")

if st.button("Predict"):
    result = app.predict([[area_sqft,bedroom,bathroom]])
    st.write(result)
