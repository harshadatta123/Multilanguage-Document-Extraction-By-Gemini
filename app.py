from dotenv import load_dotenv

load_dotenv()
import streamlit as st

import os
import google.generativeai as genai

from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

text = "Utilizing Gemini Pro AI, this project effortlessly extracts vital information + \
from diverse multilingual documents, transcending language barriers with \nprecision and + \
efficiency for enhanced productivity and decision-making."
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

def get_gemini_response(multimodal_prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(multimodal_prompt)
    return response.text

def input_image_setup(uploaded_file):
    image = Image.open(uploaded_file)
    return image


uploaded_file = st.file_uploader("Choose an image of the document: ", type = ["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width = True)


user_input = st.text_input("Enter your prompt:")

input_prompt = """
An image will be given and you will have to answer any questions based on the uploaded image. 
While answering, provide your chain-of-thought reasoning before validating it with adequate spacing.
"""

if user_input:
    response = get_gemini_response([image, input_prompt + user_input])
    st.write(str(response))
