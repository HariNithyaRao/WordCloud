import streamlit as st
import numpy as np
import wordcloud 
from collections import Counter

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1683010606819-de5d37be0b25?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1975&q=80");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

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

