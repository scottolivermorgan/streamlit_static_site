import streamlit as st
from helpers.helpers import load_css, display_card
from helpers.helpers import load_footer, load_navbar_style

load_navbar_style()


# Load css stylesheet
load_css("./assets/static/css/styles.css")

# Create two columns with a 50:50 width ratio
col1, col2 = st.columns(2)

with col1:
    display_card(
        "https://via.placeholder.com/300x200",
        "Card Title",
        "This is a description of the card content. It can be a short summary or some important details.",
    )
with col2:
    display_card(
        "https://via.placeholder.com/300x200",
        "Using adsorption kinetics to assemble vertically \
				 aligned nanorods at liquid interfaces for\
				 metamaterial applications.",
        "Vertically aligned monolayers of metallic nanorods have a wide \
                  range of applications as metamaterials or in surface enhanced Raman \
				  spectroscopy. However the fabrication of such structures using current \
				  top-down methods or through assembly on solid substrates is either \
				  difficult to scale up or have limited possibilities for further \
				  modification after assembly. The aim of this paper is to use the adsorption\
				  kinetics of cylindrical nanorods at a liquid interface as a novel route \
				  for assembling vertically aligned nanorod arrays that overcomes these problems.",
    )

# Create two columns with a 50:50 width ratio
col3, col4 = st.columns(2)

with col3:
    display_card(
        "https://via.placeholder.com/300x200",
        "Card Title",
        "This is a description of the card content. It can be a short summary or some important details.",
    )
with col4:
    display_card(
        "https://via.placeholder.com/300x200",
        "Card Title",
        "This is a description of the card content. It can be a short summary or some important details.",
    )


load_footer()