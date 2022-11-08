import streamlit as st
from PIL import Image
st.title('# 우리집 강아지 뽀순이 사진')
image = Image.open('뽀순이 사진.jpg')
st.image(image)
image2 = Image.open('뽀순이 사진2.jpg')
image3 = Image.open('뽀순이 사진3.jpg')
image4 = Image.open('뽀순이 사진4.jpg')
image5 = Image.open('뽀순이 사진5.jpg')
image6 = Image.open('뽀순이 사진6.jpg')
st.image(image2)
st.image(image3)
st.image(image4)
st.image(image5)
st.image(image6, caption='내 카메라')

video_file = open('뽀순이 영상.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)