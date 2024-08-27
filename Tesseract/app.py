import streamlit as st
import pytesseract
from PIL import Image


st.write("## Tesseract OCR \n A simple Image to Text Application")

#TODO: Limit input to supported image files
file = st.file_uploader("Choose a file", type=['png', 'jpg'])

@st.cache_data
def transcribe(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)

if file is not None:
    st.write("Image uploaded succesfully!")

    st.write("### Recognized Text")
    ocr_text = transcribe(file)
    ocr_text

