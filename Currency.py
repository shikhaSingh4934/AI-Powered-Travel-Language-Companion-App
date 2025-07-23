import requests
import streamlit as st

def get_exchange_rates(EXCHANGE_RATE_API_KEY):
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("conversion_rates", {})
        else:
            return {"error": f"Error fetching exchange rates: {response.status_code}, {response.text}"}
    except Exception as e:
        return {"error": str(e)}

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    try:
        from_rate = exchange_rates.get(from_currency)
        to_rate = exchange_rates.get(to_currency)
        if from_rate and to_rate:
            converted_amount = (amount / from_rate) * to_rate
            return round(converted_amount, 2)
        else:
            return "Invalid currency codes"
    except Exception as e:
        return str(e)

def currency_converter_app(EXCHANGE_RATE_API_KEY):
    st.title("Currency Converter")

    exchange_rates = get_exchange_rates(EXCHANGE_RATE_API_KEY)
    if "error" in exchange_rates:
        st.error(f"Error: {exchange_rates['error']}")
        return

    amount = st.number_input("Enter amount", min_value=0.01, value=1.00)
    from_currency = st.selectbox("From Currency", list(exchange_rates.keys()))
    to_currency = st.selectbox("To Currency", list(exchange_rates.keys()))

    if st.button("Convert"):
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        st.write(f"*{amount} {from_currency} = {converted_amount} {to_currency}*")

EXCHANGE_RATE_API_KEY = "1ece9901af5b5b236916f82c"  # Replace with your actual API key
currency_converter_app(st.secrets['EXCHANGE_RATE_API_KEY'])