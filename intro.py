import streamlit as st

st.title("We are learning Deployment.")
st.write("1+5=", 1+5)

agree = st.checkbox("I agree with Mohit!")

if agree:
    st.write("You're awesome!")



genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"],
)

if genre == "Comedy":
    st.write("You like comedy. Haha")