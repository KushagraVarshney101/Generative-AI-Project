from dotenv import load_dotenv
load_dotenv() ## for loading enviornment variables

import streamlit as st 
import os
import google.generativeai as GENAI

GENAI.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Loading Gemini

model=GENAI.GenerativeModel("gemini-pro")
def AI_response(question):
    response = model.generate_content(question)
    return response.text


## Initialaizing app

st.set_page_config(page_title = "Text AI")
st.header("Insight")
input = st.text_input("Input: ", key = "input")
submit = st.button(" ➡️ ")

if submit:
    response = AI_response(input)
    st.subheader("Your Answer is")
    st.write(response) 
