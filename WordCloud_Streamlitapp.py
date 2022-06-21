def calculate_frequencies(s):
    cloud = w.WordCloud()
    cloud.generate_from_frequencies(Counter(s))
    return cloud.to_array()

import streamlit as st
import numpy as np
import wordcloud as w
import io
import sys
from collections import Counter

st.title("WElCOME TO WORDCLOUD🖼️")
st.write("Enter some words and have fun with wordcloud 😁")
txt = st.text_input("Type your text here!")
if len(txt) != 0:
    # generate cloud
    st.balloons()
    st.image(calculate_frequencies(txt.split()))

