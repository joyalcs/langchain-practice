import requests
import streamlit as st

def get_openai_repsonse(input_text):
    response = requests.post(
        "http://localhost:8000/openai/invoke",
        json={'input': input_text}
    )
    return response.json()['output']['content']

st.title("OpenAI Essay Generator")
input_text = st.text_input("Enter a topic for the essay:")

if input_text:
    st.write(get_openai_repsonse(input_text))