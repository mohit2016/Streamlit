import streamlit as st

st.header("Basic Calculator")

def sqaure(num):
    return num*num

number = st.number_input("Insert a number")
st.write("The current number is ", number)

if st.button("Calculate Square:"):
    result = sqaure(number)
    st.subheader(result)