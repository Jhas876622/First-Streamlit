import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# -----------------------------------------------
# Title
st.title("🎬📷 Audio, Video, Image & CSV Uploader")
st.markdown("Upload and display media files interactively")

# -----------------------------------------------
# 1. Upload and Display Image
st.subheader("🖼️ Upload an Image")
image_file = st.file_uploader("Upload Image", type=["png", "jpeg", "jpg"])
if image_file is not None:
    st.write({
        'file_name': image_file.name,
        'file_type': image_file.type,
        'file_size': image_file.size
    })
    img = Image.open(image_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

# -----------------------------------------------
# 2. Upload and Play Audio
st.subheader("🎵 Upload an Audio File")
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"], key="audio")
if audio_file is not None:
    st.write({
        'file_name': audio_file.name,
        'file_type': audio_file.type,
        'file_size': audio_file.size
    })
    st.audio(audio_file, format='audio/mp3')

# -----------------------------------------------
# 3. Upload and Play Video
st.subheader("🎥 Upload a Video File")
video_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"], key="video")
if video_file is not None:
    st.write({
        'file_name': video_file.name,
        'file_type': video_file.type,
        'file_size': video_file.size
    })
    st.video(video_file)

# -----------------------------------------------
# 4. Upload and Display CSV
st.subheader("📊 Upload a CSV File")
csv_file = st.file_uploader("Upload CSV", type=["csv"], key="csv")
if csv_file is not None:
    st.write({
        'file_name': csv_file.name,
        'file_type': csv_file.type,
        'file_size': csv_file.size
    })
    df = pd.read_csv(csv_file)
    st.dataframe(df)

# -----------------------------------------------
# 5. Remote Image Display (Optional Static Image)
st.subheader("🌐 Display Image from Link")
st.image("https://media.geeksforgeeks.org/gfg-gg-logo.svg", width=700, caption="GFG Logo from Web")
