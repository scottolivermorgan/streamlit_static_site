import streamlit as st

# HTML + CSS code for the footer component
footer_html = """
    <footer style="text-align: center; padding: 10px; background-color: #f1f1f1; bottom: 0; width: 100%;">
        <div style="margin-bottom: 10px;">
            <a href="https://www.facebook.com/Swarm-Labs-102522568202848" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/facebook-new.png" style="width: 25px; height: 25px;">
            </a>
            <a href="https://twitter.com/SwarmLtd" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/twitter--v1.png" style="width: 25px; height: 25px;">
            </a>
            <a href="https://www.linkedin.com/in/chris-lowe-1a63881b2/" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/linkedin.png" style="width: 25px; height: 25px;">
            </a>
            <a href="https://www.instagram.com/swarmlabs" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/instagram-new.png" style="width: 25px; height: 25px;">
            </a>
            <a href="https://www.youtube.com/channel/UC4xdb2kD3QfE5TkDHT8x71w/featured" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/youtube-play.png" style="width: 25px; height: 25px;">
            </a>
            <a href="https://github.com/scottolivermorgan?tab=repositories" target="_blank">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" style="width: 25px; height: 25px;">
            </a>
        </div>
        <sub>© 2023 Copyright</sub>
        <br/>
        <sub>Swarm Labs</sub>
    </footer>
"""

# Render the HTML component in the Streamlit app
st.components.v1.html(footer_html, height=120)
