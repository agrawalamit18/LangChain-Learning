import streamlit as st
import os
import helloWorld  as hw
st.title("LangChain Learning App")
country_name = st.text_input("Enter a country name:")
if st.button("Get Info"):
    response = hw.chain.invoke({"countryname": country_name})
    st.write("Capital:", response["capital_name"])
    st.write("Population:", response["population"]) 