import streamlit as st
st.header(" :orange[7th AIR] in Gokart Design championship held in Buddha International Circuit,Greator Noida.:trophy:")
st.subheader("Role - :blue[Manufacturing and Analysis]")
with st.expander("See explanation"):
    st.markdown('An extra innovative project.')
    with open("gkdccerti.jpg", "rb") as file:
        st.download_button(":green[Download Certificate]" , file )
    tab1, tab2 , tab3 = st.tabs(["Photos", "Videos" , "Award "])
    tab1.image("g1.jpg")
    tab1.image("g2.jpg")
    tab1.image("g3.jpg")
    tab1.image("g4.jpg")
    tab1.image("g5.jpg")
    tab1.image("g7.jpg")
    tab1.image("g8.jpg")
    tab1.image("g9.png")
    tab1.image("g10.png")
    tab1.image("g11.png")
    tab1.image("g12.png")
    
    video_file = open('gv1.mp4', 'rb')
    video_bytes = video_file.read()
    tab2.video(video_bytes)

    video_file = open('gv2.mp4', 'rb')
    video_bytes = video_file.read()
    tab2.video(video_bytes)

    video_file = open('gv3.mp4', 'rb')
    video_bytes = video_file.read()
    tab2.video(video_bytes)

    video_file = open('gv4.mp4', 'rb')
    video_bytes = video_file.read()
    tab2.video(video_bytes)

    video_file = open('gvstu.mp4', 'rb')
    video_bytes = video_file.read()
    tab2.video(video_bytes)

    tab3.image("g88.jpg")
    tab3.image("gkdccerti.jpg")
    tab3.balloons()






