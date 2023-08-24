import streamlit as st
st.header("CarlingDhoot pvt ltd, Auranagabad (M.H.)")
st.subheader("Graduate Apprentice Trainee :- Production Engineer")
with st.expander("See explanation"):
    st.markdown('From Dec 2019 to March 2020 :-In PPC department used equipment to assist with manufacturing- packaging- and other steps along a :blue[production assembly line]. Worked with pneumatic SPM machines and :blue[poka_yoke] on fixtures to reduce human errors.Deployed :blue[KAIZEN] and :blue[6SIGMA].')
with open("cdicerti.jpg", "rb") as file:
   st.download_button(":green[Download Certificate]" , file )
with open("jobreport.docx", "rb") as file:
   st.download_button(":green[Download Job Report]" , file )

tab1, tab2, tab3 , tab4 , tab5 , tab6 = st.tabs(["1","2","3","4","5","6"])

with tab1:
   st.image("cd1.jpg", width=400)

with tab2:
   st.image("cd2.jpg", width=400)

with tab3:
   st.image("cd3.jpg", width=400)

with tab4:
   st.image("cd4.jpg", width=400)

with tab5:
   st.image("cd5.jpg", width=400)

with tab6:
   st.image("cd6.jpg", width=400)


