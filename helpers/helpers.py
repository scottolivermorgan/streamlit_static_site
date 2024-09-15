import streamlit as st
import base64
from pathlib import Path


def load_css(css_file_path):
    """
    Function to load a CSS file and inject it into the Streamlit app.

    Parameters:
    css_file_path (str): Path to the CSS file.
    """
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_footer():
    footer = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
    
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #382e2c;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #000000;
    }
    .footer .external-links a {
        margin: 0 5px;  /* Add horizontal spacing between icons */
    }
    </style>
    <div class="footer">
        <div class="external-links">
            <a href="https://www.youtube.com/channel/UC4xdb2kD3QfE5TkDHT8x71w/featured" target="_blank" rel="noopener noreferrer">
                <i class="fa-brands fa-youtube fa-xl" style="color: #ffffff;"></i>
            </a>
            <a href="https://www.instagram.com/swarmlabs" target="_blank" rel="noopener noreferrer">
                <i class="fa-brands fa-instagram fa-xl" style="color: #ffffff;"></i>
            </a>
            <a href="https://github.com/scottolivermorgan?tab=repositories" target="_blank" rel="noopener noreferrer">
                <i class="fa-brands fa-github fa-xl" style="color: #ffffff;"></i>
            </a>
            <a href="https://twitter.com/SwarmLtd" target="_blank" rel="noopener noreferrer">
                <i class="fa-brands fa-twitter fa-xl" style="color: #ffffff;"></i>
            </a>
            <a href="https://www.facebook.com/Swarm-Labs-102522568202848" target="_blank" rel="noopener noreferrer">
                <i class="fa-brands fa-facebook fa-xl" style="color: #ffffff;"></i>
            <a/>
            <a href="https://www.linkedin.com/in/chris-lowe-1a63881b2/" target="_blank" rel="noopener noreferrer">
                <i class="fa-brands fa-linkedin-in fa-xl" style="color: #ffffff;"></i>
            </a>
        </div>
        <sub style="color: white;">© 2024 Copyright Swarm Labs</sub>

    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)


def load_navbar_style():
    # Hide the top right menu and Streamlit footer
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        /* Change background color of the sidebar */
        .st-emotion-cache-6qob1r.eczjsme11 {   /* The class name may change depending on Streamlit version */
            background-color: rgba(56, 46, 44, 0.7); /* Set your desired color */
        }

        .st-emotion-cache-1rtdyuf.eczjsme13 {
        color: white;
        }
        .st-emotion-cache-6tkfeg.eczjsme13 {
        color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def img_to_bytes(img_path):
    """
    Converts an image file to a base64-encoded string.

    Args:
        img_path (str): The path to the image file.

    Returns:
        str: The base64-encoded string representation of the image.
    """
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path):
    """
    Converts an image file to an HTML `<img>` tag with embedded base64 data.

    Args:
        img_path (str): The file path to the image that needs to be converted.

    Returns:
        str: An HTML string containing an `<img>` tag with the image data encoded in base64.

    Example:
        >>> img_html = img_to_html('path/to/image.png')
        >>> print(img_html)
        "<img src='data:image/png;base64,...' class='img-fluid'>"
    """
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
        img_to_bytes(img_path)
    )
    return img_html


def display_card(image_src: str, title: str, description: str):
    """
    Displays a customizable card with an image, title, and description in a Streamlit app.

    Args:
        image_src (str): The source URL or file path of the image to be displayed on the card.
        title (str): The title text to be displayed on the card.
        description (str): The paragraph text to be displayed as the card's content.

    Example:
        card("https://via.placeholder.com/300x200", "Card Title", "This is a description of the card content. It can be a short summary or some important details.")
    """
    # Create a container for the card with dynamic inputs
    card_html = f"""
    <div class="material-card">
        <img src="{image_src}" alt="Card Image">
        <h4>{title}</h4>
        <p>{description}</p>
    </div>
    """

    # Display the card in Streamlit
    st.markdown(card_html, unsafe_allow_html=True)


# def profile_card(image_src: str,
#                 title: str,
#                 postfix: str,
#                 role: str,
#                 description: str,
#                 linkedin_url: str):
#    """
#    Displays a customizable card with an image, title, and description in a Streamlit app.
#
#    Args:
#        image_src (str): The source URL or file path of the image to be displayed on the card.
#        title (str): The title text to be displayed on the card.
#        description (str): The paragraph text to be displayed as the card's content.
#
#    Example:
#        card("https://via.placeholder.com/300x200", "Card Title", "This is a description of the card content. It can be a short summary or some important details.")
#    """
#
#    # Add FontAwesome CDN to the app
#    st.markdown("""
#        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    """, unsafe_allow_html=True)
#
#    card_html = f"""
#    <div class="material-card">
#        {img_to_html(image_src)}
#        <center>
#            <h4>{title}<sup>{postfix}<sup/></h4>
#        <center/>
#        <h5>{role}<h5/>
#        <p>{description}</p>
#        <a href="{linkedin_url}" target="_blank">
#            <i class="fa-brands fa-linkedin" style="font-size:30px;color:#0e76a8;"></i>
#        </a>
#    </div>
#    """
#
#    # Display the card in Streamlit
#    st.markdown(card_html, unsafe_allow_html=True)


# def profile_card(image_src: str,
#                 title: str,
#                 postfix: str,
#                 role: str,
#                 description: str,
#                 links: dict):
#    """
#    Displays a customizable card with an image, title, and description in a Streamlit app.
#
#    Args:
#        image_src (str): The source URL or file path of the image to be displayed on the card.
#        title (str): The title text to be displayed on the card.
#        postfix (str): A postfix to display next to the title (like a superscript).
#        role (str): The role or position of the person.
#        description (str): The paragraph text to be displayed as the card's content.
#        links (dict): A dictionary where keys are FontAwesome icon classes and values are corresponding URLs.
#
#    Example:
#        profile_card("https://via.placeholder.com/300x200", "Card Title", "PhD", "Data Scientist",
#                     "This is a description of the card content.",
#                     {"fa-brands fa-linkedin": "https://linkedin.com/in/username",
#                      "fa-brands fa-github": "https://github.com/username"})
#    """
#
#    # Add FontAwesome CDN to the app
#    st.markdown("""
#        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    """, unsafe_allow_html=True)
#
#    # Generate HTML for icons based on provided links
#    icons_html = "".join(
#        f'<a href="{url}" target="_blank" style="margin: 0 10px;">'
#        #f'<i class="{icon_class}" style="font-size:30px;color:#0e76a8;"></i></a>'
#        f'<i class="{icon_class}"></i></a>'
#        for icon_class, url in links.items() if url
#    )
#
#    card_html = f"""
#    <div class="material-card">
#        {img_to_html(image_src)}
#        <h4>{title}<sup>{postfix}</sup></h4>
#        <h5>{role}</h5>
#        <p>{description}</p>
#        <div style="margin-top: 10px;">
#            {icons_html}
#        </div>
#    </div>
#    """
#
#    st.markdown(card_html, unsafe_allow_html=True)
def profile_card(
    image_src: str, title: str, postfix: str, role: str, description: str, links: dict
):
    """
    Displays a customizable card with an image, title, and description in a Streamlit app.

    Args:
        image_src (str): The source URL or file path of the image to be displayed on the card.
        title (str): The title text to be displayed on the card.
        postfix (str): A postfix to display next to the title (like a superscript).
        role (str): The role or position of the person.
        description (str): The paragraph text to be displayed as the card's content.
        links (dict): A dictionary where keys are FontAwesome icon classes and values are corresponding URLs.
    """

    # Add FontAwesome CDN to the app
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            .profile-card-container {
                display: flex;
                justify-content: center;
                align-items: stretch;
                height: 100%;
            }
            .profile-card {
                padding: 20px;
                text-align: center;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                width: 100%;
                box-sizing: border-box;
            }
            .profile-card h4, .profile-card h5, .profile-card p {
                margin: 10px 0;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Generate HTML for icons based on provided links
    icons_html = "".join(
        f'<a href="{url}" target="_blank" style="margin: 0 10px;">'
        f'<i class="{icon_class}"></i></a>'
        for icon_class, url in links.items()
        if url
    )

    # Card HTML structure
    card_html = f"""
    <div class="profile-card-container">
        <div class="profile-card">
            {img_to_html(image_src)}
            <h4>{title}<sup>{postfix}</sup></h4>
            <h5>{role}</h5>
            <p>{description}</p>
            <div style="margin-top: 10px;">
                {icons_html}
            </div>
        </div>
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)
