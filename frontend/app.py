import streamlit as st
import requests

st.title("House price prediction")

area=st.number_input("Enter area")
bedrooms=st.number_input("Enter bedrooms")
age=st.number_input("Enter age")

if st.button("Predict"):
    data={"area":area, "bedrooms":bedrooms, "age":age}
    response=requests.post(
        "https://house-price-detection-end-to-end-project.onrender.com/predict",
        json=data
    )
    result=response.json()     # received prediction from fastapi 
    #st.write(result)           it use for debugging purpose to see that what the actual json is return
    st.success(f"Predicted Price range:{result['predicted_price']}")


