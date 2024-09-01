import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_base64 = get_base64_image("assets/static/logo.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
        width: 50%;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
