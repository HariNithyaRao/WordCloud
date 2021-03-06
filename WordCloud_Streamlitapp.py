import streamlit as st
import numpy as np
import wordcloud 
from collections import Counter

def calculate_frequencies(s):
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(Counter(s))
    return cloud.to_array()

st.title("WElCOME TO WORDCLOUD🖼️")
st.write("Enter some words and have fun with wordcloud 😁")
txt = st.text_input("Type your text here!")
if len(txt) != 0:
    # generate cloud
    st.balloons()
    st.image(calculate_frequencies(txt.split()))

