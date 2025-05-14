import streamlit as st

st.set_page_config(page_title="Education - Colin Bertrand", 
                   layout="wide")


st.title("Education")
"---"

#defining columns
col1, col2, col3 = st.columns([0.3, 0.1, 0.75])

#text
with col3:
    st.header("B.S. in Data Science + Information Science")
    st.subheader("Minor in Computer Science")
    st.markdown("Expected Graduation May 2026")
    with st.container(border=True):
        st.subheader("Relevant Coursework:")
        st.markdown("Modeling & Learning in Data Science, Algorithms and Data Structures for Data Science, Programming for Info Problems, Linear Algebra in Data " \
        "Science, Analytical Foundations for Information Problems, Concepts of Machine Learning, Human Computer Interaction...")
    with st.container(border=True):
        st.subheader("Campus Involvement:")
        st.markdown("Marching Illini, Illini Drumline, Men's Basketball Band")

with col1:
    st.image("images/University-Seal.png", use_container_width=True)
    with st.container(border=True):
        cola, colb, colc = st.columns([1, 2, 1])
        with colb:
            st.caption("<p style='text-align: center; font-size:15px;'>University of Illinois in Urbana-Champaign</h1>", unsafe_allow_html=True)
"---"
st.header("Certifications", )
cola, colb = st.columns([2, 1])
with cola:
    st.image("images/microcredential_stat107-sp23_Colin_Bertrand.png", use_container_width=True)
with colb:
    st.subheader("Data Science DISCOVERY @ UIUC")
    st.link_button("Certification Link", "https://d7.cs.illinois.edu/badges/stat107-sp23-1PiruLlJ7nA9Y7wV06HDwHfRQDbgP6/", use_container_width=True)
    st.markdown("This microcredential acknowledges that Colin Bertrand demonstrated mastery in Data Science DISCOVERY at The University of Illinois "
    "and was issued this credential on May 23, 2023. To earn this credential, mastery was demonstrated in 42 areas of Data Science")
"---"

    
    