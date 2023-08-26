import streamlit as st
st.header("Rainwater Harvesting with Power Generation")
st.subheader("Role: Design and Analysis")
with st.expander("See explanation"):
    st.markdown('An innovative 5 month Minor_Project under curriculum of Univeristy.')
with open("minor1.pdf", "rb") as file:
   st.download_button(":green[Download Project File]" , file )
with open("minor1.pptx", "rb") as file:
   st.download_button(":green[Download Project Presentation]" , file )


