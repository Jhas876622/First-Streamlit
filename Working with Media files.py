import pandas as pd
import streamlit as st
from PIL import Image

# Image from Path
st.title('1. Image from Path')
img = Image.open(r'C:\Users\Satyam Jha\Desktop\DATA SCIENCE\STREAMLIT\Models.jpeg')
st.image(img)

# Image from Link
st.title('2. Image from Link')
st.image('https://media.geeksforgeeks.org/gfg-gg-logo.svg', width=700)

# Video
st.title('3. Video')
video_file = open(r'C:\Users\Satyam Jha\Desktop\DATA SCIENCE\STREAMLIT\video.mp4', 'rb')
st.video(video_file, start_time=10)

# Audio
st.title('4. Audio')
audio_file = open(r'C:\Users\Satyam Jha\Desktop\DATA SCIENCE\STREAMLIT\sample.mp3', 'rb')
st.audio(audio_file.read())


#FILE UPLOADING

#1.Image
st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload Image', type = ['png','jpeg','jpg'])
if img_file is not None:
    st.write(type(img_file))

    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                     'file_size' : img_file.size}
    st.write(file_details)

    st.image(Image.open(img_file))
#2.Audio
st.subheader('2. Uploading an Audio')
img_file = st.file_uploader('Upload Audio', type = ['wav','mp3'])
if img_file is not None:
    st.write(type(img_file))

    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                     'file_size' : img_file.size}
    st.write(img_file)
    st.audio(img_file)

#3.Video
st.subheader('2. Uploading an Video')
img_file = st.file_uploader('Upload Video', type = ['wav','mp3'])
if img_file is not None:
    st.write(type(img_file))

    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                     'file_size' : img_file.size}
    st.write(img_file)
    st.video(img_file)

#4.CSV
st.subheader('2. Uploading a CSV')
img_file = st.file_uploader('Upload CSV', type = ['Spreadsheet','text'])
if img_file is not None:
    st.write(type(img_file))

    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                     'file_size' : img_file.size}
    st.write(img_file)

    st.dataframe(img_file)
