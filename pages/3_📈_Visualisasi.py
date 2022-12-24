from PIL import Image
import streamlit as st

st.title("Visualisasi")

image = Image.open('foo.png')

st.image(image, caption='Decision Tree')
