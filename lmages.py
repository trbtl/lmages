# pip install streamlit Pillow
# streamlit run images.py
# python -m venv venv
# venv\Scripts\activate
# pip freeze > requirements.txt

import streamlit as st
from datetime import datetime
import os
from PIL import Image

# Set the folder path where your images are stored
folder_path = './images'  # Adjust this path to your images folder

# Display current date and time in the sidebar
st.sidebar.header("Current Date & Time")
st.sidebar.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Display names of picture files in the sidebar
st.sidebar.header("Picture Files")
pictures = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
for pic in pictures:
    st.sidebar.write(pic)

# Input field for comments
comment = st.text_input("Leave a comment:")

# Display images
st.header("Gallery")
for pic in pictures:
    image_path = os.path.join(folder_path, pic)
    image = Image.open(image_path)
    st.image(image, caption=pic, use_column_width=True)
