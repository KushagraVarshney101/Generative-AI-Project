from dotenv import load_dotenv
load_dotenv() ## for loading enviornment variables

import streamlit as st 
import os
import google.generativeai as GENAI
from PIL import Image

GENAI.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Loading Gemini_Vision

model=GENAI.GenerativeModel("gemini-pro-vision")
def AI_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

## Initialaizing app

st.set_page_config(page_title = "Image AI")
st.header("PixelSense")
input = st.text_input("Input: ", key = "input")

upload_image = st.file_uploader("Choose Your Image " , type = ["jpg", "jpeg", "png"] )
image = ""
if upload_image is not None:
    image = Image.open(upload_image)
    st.image(image, caption="Uploaded Image",  use_column_width = True)
    
submit = st.button(" ➡️ ")
if submit:
    response = AI_response(input,image)
    st.subheader("Description")
    st.write(response)



