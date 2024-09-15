import streamlit as st
from helpers.helpers import load_css, profile_card, load_footer, load_navbar_style

# Load css stylesheet
load_css("./assets/static/css/styles.css")
load_navbar_style()
load_footer()

# Create first row with two columns with a 50:50 width ratio
col1, col2 = st.columns(2)

with col1:
    profile_card(
        "./assets/static/images/staff_profiles/scott.png",
        "Scott Morgan",
        " PhD.",
        "Principle Scientist & Engineer",
        "Passionate surfer whose enthusiasm far exceeds his skill",
        {
            "fa-brands fa-linkedin": "https://www.linkedin.com/in/scott-oliver-morgan/",
            "fa-brands fa-google": "https://scholar.google.com/citations?user=LI_qhRsAAAAJ&hl=en",
            "fa-brands fa-github": "https://github.com/scottolivermorgan",
        },
    )
with col2:
    profile_card(
        "./assets/static/images/staff_profiles/chris.png",
        "Chris Lowe",
        " Mphys.",
        "Scientific Consultant",
        "Avid motorbike fan, technologist & wannabe chef.",
        {"fa-brands fa-linkedin": "https://www.linkedin.com/in/chris-lowe-86221899/"},
    )

# Create second row with two columns with a 50:50 width ratio
col3, col4 = st.columns(2)

with col3:
    profile_card(
        "./assets/static/images/staff_profiles/jacqueline.png",
        "Jacqueline Maxfield",
        " Bsc. Hons",
        "Lead Branding and Design",
        "Graphic designer & cat lover with an obsession for typography.",
        {"fa-brands fa-linkedin": "https://www.linkedin.com/in/maxfieldjacqueline/"},
    )
with col4:
    profile_card(
        "./assets/static/images/staff_profiles/charlie.png",
        "Charlie Street",
        "",
        "Sales Lead",
        "Tenacious outdoorsman, forager and spear fisherman.",
        {
            "fa-brands fa-linkedin": "https://www.linkedin.com/in/charlie-heath-a3a435135/"
        },
    )
