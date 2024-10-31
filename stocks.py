import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer")

ticker_symbol = st.text_input("Please enter the script name", "AAPL")
ticker_data = yf.Ticker(ticker_symbol)

col1, col2= st.columns(2)

with col1:
    start_date = st.date_input("Please enter the starting date", datetime.datetime(2022, 1,1))    

with col2:
    end_date = st.date_input("Please enter the starting date", datetime.datetime(2023, 1,1))


ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)


st.success(ticker_symbol)
st.write("Here's the raw day wise stock movement:")
st.dataframe(ticker_df)


st.header("Price movement over time")
st.line_chart(ticker_df['Close'])


st.header("Volume movement over time")
st.bar_chart(ticker_df['Volume'])