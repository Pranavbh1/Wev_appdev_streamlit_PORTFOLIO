import streamlit as st
st.header("SKILLSET(Data Science):  :computer:") 
col1, col2, col3 = st.columns(3)
with col3:
   st.button("Statistics")
   st.button("SQL")
   st.button("web app dev[streamlit]:computer:")
   st.button("Python Programming Leanguage :snake:") 
   

with col2:
   st.button("Machine Learning")
   st.button("Deep Learning")
   st.button("Tableau")
   st.button("NLP ")

with col1:
   st.button("Computer Vision")
   st.button("AI ")
   st.button("Data Science")
   st.button("Data Analysis")
   st.button("Mechatronics")



st.header("SKILLSET(Mechanical):  :hammer_and_wrench:")
col3, col4 = st.columns(2)

with col4:

    with open("CertiCreo.pdf", "rb") as file:
        st.download_button(":green[PTC Creo Certification(download)]" , file )

    st.button("CAD")
    st.button("CAM")
with col3:

    st.button("Product Design")
    st.button("Solid Works")
    st.button("MS Office")

st.header("Personal Skills")
col5,col6 = st.columns(2)
with col5:
    st.button("Leadership(Project)")
    st.button("Management(Project)")
with col6:
    st.button("Quick Learner")
    st.button("Adaptive")


st.header("Certifications")
st.subheader("TATA steel - Fuel and Combustion")
with st.expander("See explanation"):
    st.markdown('Issued on June 2020 :- An e-learning certification on FUEL & COMBUSTION by TATA STEEL')
    with open("TScerti.jpg", "rb") as file:
        st.download_button(":green[Download Certificate]" , file )



