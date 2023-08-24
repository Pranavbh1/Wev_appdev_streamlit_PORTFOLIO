import streamlit as st 
st.header("Educational Qualification :open_book:")
tab1, tab2 = st.tabs(["Pursuing", "Pursued"])

tab1.subheader("ASPIRING DATA SCIENTIST")
tab1.caption("INNOMATICS RESEARCH LABS , HYDERABAD ")
tab1.code("IBM Certified Data Scientist Course (From June 2023)")
tab1.graphviz_chart('''
    digraph {
        Beginner -> Python_Programming_Language
        Python_Programming_Language -> Statistics
        Statistics -> Python_Data_Analysis
        Python_Data_Analysis -> SQL
        SQL -> Tableau
        Tableau -> ML
        ML -> DL
        DL -> Compter_Vision
        Compter_Vision -> NLP
        NLP -> DATA_SCIENTIST
    }
''')

mydetails = {
  "Degree - B.Tech(Mechanical Engineering with Specialisation in MECHATRONICS)" : {
    "Institute_Name" : "Medicaps University",
    "year" : '2016-2020' ,
    "Percent" : "69.5%"
  },
  "Higher_Secondary_12th" : {
    "Institute_Name" : "Priyarshini Hr Sec School",
    "year" : '2015-2016' ,
    "Percent" : "79.5%"
  },
  "Secondary_10th" : {
    "Institute_Name" : "St. Judes Hr Sec School",
    "year" : '2013-2014' ,
    "Percent" : "77.9%"
  }
}
tab2.table(mydetails)


