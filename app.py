import streamlit as st
import pandas as pd

st.write(
    """
    # My first app
    Hello *world!*     
    """
)

with st.chat_message("user"):
    st.write("Hello 👋")
