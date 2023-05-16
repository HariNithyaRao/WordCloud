import streamlit as st
import numpy as np
import wordcloud 
from collections import Counter

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()

def calculate_frequencies(s):
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(Counter(s))
    return cloud.to_array()

st.title("WELCOME TO WORDCLOUD🖼️")
st.write("Enter some words and have fun with wordcloud 😁")
txt = st.text_input("Type your text here!")
if len(txt) != 0:
    # generate cloud
    st.balloons()
    st.image(calculate_frequencies(txt.split()))

