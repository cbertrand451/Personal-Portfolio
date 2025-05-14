import streamlit as st

st.set_page_config(page_title="Contact - Colin Bertrand", 
                   layout="wide")

#opening resume
with open("misc_files/Colin Bertrand Resume.pdf", "rb") as pdf_file:
    PDF = pdf_file.read()

col1, col2, mid, col3, col4 = st.columns([1, 2, 0.25, 2, 1])

with col2:
    st.image("images/Headshot.png", use_container_width=True)
with col3:
    st.title("Colin Bertrand")
    st.markdown("**DS + IS Major @ UIUC**")
    st.download_button(
        label='Download Resume',
        data= PDF, 
        file_name='Colin Bertrand Resume.pdf', 
        mime= 'application/pdf', 
        use_container_width=True
    )
    cola, colb = st.columns([1, 1])
    with cola:
        st.link_button('LinkedIn', 'https://www.linkedin.com/in/colin-bertrand-512138265/', use_container_width=True)
        #st.image("images/linkedin.png", use_container_width=True)
    with colb:
        st.link_button("GitHub", "https://github.com/cbertrand451", use_container_width=True)
        #st.image("images/github.png", use_container_width=True)
    st.subheader("Thank you for stopping by!")
    st.markdown("Feel free to contact me at the email address below:")
    st.markdown("**colinbb2@illinois.edu**")
"---"
