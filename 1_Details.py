import streamlit as st
st.header('--------------------:blue[PORTFOLIO]--------------------')
from PIL import Image

col1, col2, col3 = st.columns(3)
with col3:
   st.header(" ")
   image = Image.open('p1.jpg')
   st.image(image ,width=200)
with col1:
   st.subheader(':orange[PRANAV BHAWSAR]')

code ='''Address :: 101 BTI ROAD, KHARGONE (451001), M.P.
Mobile :: 8982667641/8989667641'''
st.code(code, language='python')
st.subheader('www.linkedin.com/in/pranav-bhawsar-996328166')
st.subheader('https://github.com/Pranavbh1')

st.sidebar.markdown('<a href="mailto:pranavbhawsar@outlook.com">Contact us !</a>', unsafe_allow_html=True)
with open("R.pdf", "rb") as file:
   st.sidebar.download_button(" :green[Download Resume]" , file )
