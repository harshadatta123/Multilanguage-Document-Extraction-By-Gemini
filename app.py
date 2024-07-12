### Health Management App

## Function to load Google Gemini Pro Vision API and get response
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables
import streamlit as st

import os
import google.generativeai as genai

from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# initilize streamlit app
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

text = "Utilizing Gemini Pro AI, this project effortlessly extracts vital information + \
from diverse multilingual documents, transcending language barriers with \nprecision and + \
efficiency for enhanced productivity and decision-making."
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

def get_gemini_response(multimodal_prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(multimodal_prompt)
    return response.text

def input_image_setup(uploaded_file):
    image = Image.open(uploaded_file)
    return image

# input = st.text_input("Input Prompt: ", key = "input")
uploaded_file = st.file_uploader("Choose an image of the document: ", type = ["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width = True)
submit = st.button("Tell me about the document")

input_prompt = """
You are an expert in understanding invoices.
We will upload an image as invoice and you will have to answer any questions based on the uploaded invoice image.
"""

# if submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response([image_data, input_prompt])
    st.subheader("The response is")
    st.write(str(response))


