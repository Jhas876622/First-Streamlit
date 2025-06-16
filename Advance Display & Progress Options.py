import time
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(page_title = "Happy birthday Satyam!", page_icon = '♥️', layout = 'centered')

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎂 Happy Birthday Satyam! 🎉</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Wishing you joy, success and celebration today and always! 🥳</h3>", unsafe_allow_html=True)

st.balloons()
st.snow()

st.markdown("### Here's a surprise for you! 🎁")

with st.spinner("Loading surprise..."):
    time.sleep(2)
    st.success("Ta-da! 🎉 Enjoy your special day!")

# Show GIF or image
st.image("https://media.giphy.com/media/3o6ZsWb7jTslI7bY6w/giphy.gif", caption="Celebrate like a Rockstar!", use_container_width=True)

if st.button("🎵 Play Birthday Song"):
    st.markdown("[Click here to listen to the song](https://www.youtube.com/watch?v=ho08YLYDM88)", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
