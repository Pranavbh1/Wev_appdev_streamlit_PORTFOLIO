import streamlit as st

st.header(":bulb: :orange[Career] :orange[Objective] :bulb:")
st.subheader("Seeking an entry-level position as a :green[Data Scientist] where I can gain hands-on experience while developing cutting-edge solutions for the organization’s needs.")
st.sidebar.markdown('<a href="mailto:pranavbhawsar@outlook.com">Contact us !</a>', unsafe_allow_html=True)


with open("R.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open("R.pdf", "rb") as file:
   st.sidebar.download_button(":green[Download Resume]" , file )
st.image("DS.jpeg")