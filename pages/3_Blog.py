import streamlit as st
from datetime import datetime
from helpers.helpers import load_footer, load_navbar_style

load_navbar_style()
load_footer()

## Sample blog post data
#blog_posts = [
#    {
#        "title": "My First Blog Post",
#        "date": datetime(2024, 9, 1),
#        "content": """
#        This is the content of my first blog post. 
#        Here, I can write about anything I like!
#        """,
#        # "image": "path/to/image1.jpg",
#        "tags": ["streamlit", "blog", "python"],
#    },
#    {
#        "title": "Another Exciting Update",
#        "date": datetime(2024, 8, 25),
#        "content": """
#        Here's another update with more cool things to share!
#        """,
#        # "image": "path/to/image2.jpg",
#        "tags": ["update", "news"],
#    },
#]
#
## Display the blog posts
#st.title("My Blog")
#
#for post in blog_posts:
#    st.subheader(post["title"])
#    st.write(post["date"].strftime("%B %d, %Y"))
#    # st.image(post["image"])
#    st.markdown(post["content"])
#    st.write("Tags:", ", ".join(post["tags"]))
#    st.write("---")

import json

def load_posts():
    with open('./data/posts.json', 'r') as file:
        return json.load(file)
    
# Load the blog posts
posts = load_posts()

# Display a summary of blog posts
st.title("Blog")
for post in posts:
    st.subheader(post['title'])
    st.write(post['summary'])

    if st.button(f"Read more about {post['title']}", key=post['id']):
        print(post['id'])


"""
import streamlit as st
from utils.data_loader import load_posts

# Get the post ID from session state or a URL parameter
selected_post_id = st.session_state.get('selected_post_id', None)

# Load the blog posts
posts = load_posts()

if selected_post_id:
    # Find the post by its ID
    post = next(post for post in posts if post['id'] == selected_post_id)
    
    # Display the full post
    st.title(post['title'])
    st.write(post['date'])
    st.write(post['content'])
else:
    st.warning("Post not found!")

"""