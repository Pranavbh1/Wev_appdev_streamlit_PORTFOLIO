import streamlit as st

st.header("1. Ultratech Cement LTD, Dhar")
st.subheader(" :blue[INTERN] :: July - Aug 2019 (1 month)")
with st.expander("See explanation"):
    st.markdown('The cement factory internship emphasized my personality, working under professional engineers, and learning about heavy machines.')
    st.image("ultra.jpg")

st.header("2. Vtech engineering, Indore")
st.subheader(" :blue[INTERN] :: June - July 2019 (1 month)")
with st.expander("See explanation"):
    st.markdown('Went through :blue[manufacturing] and :blue[design] of various types of mechanical :blue[refinery machinery]. I also developed :blue[marketing] and :blue[selling skills].')
    with open("vtechcerti.pdf", "rb") as file:
        st.download_button(":green[Download Certificate]" , file )

st.header("3. Singaji Thermal powerstation (Dongaliya)")
st.subheader(" :blue[INTERN] :: June - June 2018 (15 Days)")
with st.expander("See explanation"):
    st.markdown('Experience of gigantic thermal machinery and thermo-chemical processes.')

st.header("4. Dgears (workshop)")
st.subheader(" :blue[ATTENDEE] :: June 2018 (5 Days)")
with st.expander("See explanation"):
    st.markdown('Hands-On Engines(AUDI V8 Engine etc.).')
    st.image("dgear.jpg")

st.header("5. Dhawal engineering, Dewas")
st.subheader(" :blue[INTERN] :: June - July 2017 (1 month )")
with st.expander("See explanation"):
    st.markdown('Got practical knowledge of gear and pipe manufacturing')
    with open("dhawal.jpg", "rb") as file:
        st.download_button(":green[Download Certificate]" , file )

