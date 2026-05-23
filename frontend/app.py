import streamlit as st
import requests

st.title("House price prediction")

area=st.number_input("Enter area")
bedrooms=st.number_input("Enter bedrooms")
age=st.number_input("Enter age")

if st.button("Predict"):
    data={"area":area, "bedrooms":bedrooms, "age":age}
    response=requests.post(
        "http://backend:8000/predict",
        json=data
    )
    result=response.json()     # received prediction from fastapi 
    st.success(f"Predicted Price:{result['predicted_price']}")

