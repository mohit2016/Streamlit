import streamlit as st
import pandas as pd
import pickle

with open ("car_pred_model", 'rb') as file:
    model = pickle.load(file)

cars_df = pd.read_csv("./cars24-car-price.csv")

st.title("Car resale Price Prediction")
st.dataframe(cars_df.head())

## Encoding Categorical features
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     500, 5000, step=100)

transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

seats = col2.selectbox("Enter the number of seats",
                       [4,5,7,9,11])


if st.button("Predict Price"):
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]

    input_features = [[2012, 2, 120000, encoded_fuel_type, encoded_transmission_type, 19.7, engine, 46.3, seats]]

    price = round(model.predict(input_features)[0], 2)
    
    st.header("Predicted price is: " + str(price) )

