import streamlit as st
from helpers.helpers import load_footer, load_navbar_style, get_base64_image

load_navbar_style()
load_footer()
image_base64 = get_base64_image("assets/static/images/logo.png")

_col1, col2, _col3 = st.columns([0.1, 0.8, 0.1])

with col2:
    st.html(
        f"""
            <img src="data:image/png;base64,{image_base64}" alt="background logo" width="480" height="361">
    """
    )
