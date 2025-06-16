import numpy as np
import pandas as pd
import streamlit as st

# Static Tabs
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])
tab1.image('https://static.streamlit.io/examples/cat.jpg', width=200)
tab2.image('https://static.streamlit.io/examples/dog.jpg', width=200)
tab3.image('https://static.streamlit.io/examples/owl.jpg', width=200)

# Upload CSV with Image URLs
uploaded_file = st.file_uploader("Upload a CSV with image links (column: img_link)", type="csv")
if uploaded_file is not None:
    imgs = pd.read_csv(uploaded_file)['img_link']

    tabs = st.tabs([f"Image {i+1}" for i in range(30)])
    for tab in tabs:
        img = imgs.sample().values[0]
        tab.image(img, width=400)
