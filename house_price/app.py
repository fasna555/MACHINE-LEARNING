import streamlit as st
import warnings
import joblib
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

model=joblib.load("house_price_predictor.kpl")
st.title("House Price Predictor")

area = st.text_input("Enter Area (sq.ft)")
bedrooms = st.text_input("Enter Number of Bedrooms")
age = st.text_input("Enter Age of House")


if st.button('predict'):
    area=int(area)
    bedrooms=int(bedrooms)
    age=int(age)
    price=model.predict([[area,bedrooms,age]])
    st.write("price :",int(price[0])," Rs")


