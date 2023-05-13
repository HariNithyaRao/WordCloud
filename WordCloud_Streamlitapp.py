import streamlit as st
import numpy as np
import wordcloud 
from collections import Counter

import streamlit as st

# Define some CSS styles
css = """
<style>
body {
  animation: colorchange 50s infinite;
}

@keyframes colorchange
{
  0%   {background: #FFC0CB;}
  25%  {background: #90EE90;}
  50%  {background: #ADD8E6;}
  75%  {background: #FFA07A;}
  100% {background: #FFC0CB;}
}
</style>
"""
st.write(css, unsafe_allow_html=True)

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

