import streamlit as st
import streamlit as st

# Add custom CSS to create a Material UI-like card
card_css = """
<style>
.material-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: 10px;
    width: 300px;
    transition: transform 0.2s ease-in-out;
}

.material-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}

.material-card img {
    width: 100%;
    height: auto;
    border-radius: 10px;
}

.material-card h3 {
    margin: 20px 0 10px 0;
    font-size: 1.5em;
    text-align: center;
}

.material-card p {
    text-align: center;
    color: #555555;
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(card_css, unsafe_allow_html=True)

# Create a container for the card
card_html = """
<div class="material-card">
    <img src="https://via.placeholder.com/300x200" alt="Card Image">
    <h3>Card Title</h3>
    <p>This is a description of the card content. It can be a short summary or some important details.</p>
</div>
"""

# Display the card in Streamlit
st.markdown(card_html, unsafe_allow_html=True)

