from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Visualisasi")

image = Image.open('foo.png')

st.image(image, caption='Decision Tree')
