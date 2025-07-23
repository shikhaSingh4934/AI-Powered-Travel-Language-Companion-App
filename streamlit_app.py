import streamlit as st

Chat_bot = st.Page("Chat_bot.py", title = "🤖 Chat")
Currency = st.Page("Currency.py", title = "💵 Currency Converter")

pg = st.navigation([Chat_bot, Currency])
st.set_page_config(page_title="Labs")

pg.run()