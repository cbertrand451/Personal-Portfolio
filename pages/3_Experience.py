import streamlit as st

st.set_page_config(page_title="Experience - Colin Bertrand", 
                   layout="wide")


st.title("Experience")
"---"
with st.container():
    pics, texts = st.columns([1, 5])
    with pics:
        st.image("images/TCS_logo_29.webp", use_container_width=True)
        st.link_button("TCS Website", "https://www.tcs.com/", use_container_width=True)
    with texts:
        st.subheader("Intern @ TCS")
        st.markdown("*June 2025 - August 2025*")
        with st.container(border=True):
            st.markdown("Coming soon...")
    "---"

with st.container():
    pics, texts = st.columns([1, 5])
    with pics:
        st.image("images/NCSA.png", use_container_width=True)
        st.link_button("NCSA Website", "https://www.ncsa.illinois.edu/", use_container_width=True)
    with texts:
        st.subheader("SPIN Intern @ NCSA")
        st.markdown("*June 2024 - July 2024*")
        with st.container(border=True):
            st.markdown("""
                        * Researched the process of Exploratory Data Analysis (EDA) 
                        * Worked with mentor discussing differences between genres of datasets and what analysis works best for them  
                        * created a Python tool which automated the process of EDA for clients and generated custom dataset reports  
                        * Supplied Stanford Endocrinologists with reports on three Diabetes-related datasets for future analysis 
                        """)
        st.markdown(":blue-badge[Python] :blue-badge[Data Analysis] :blue-badge[Data Research] :blue-badge[EDA]")
    "---"

with st.container():
    pics, texts = st.columns([1, 5])
    with pics:
        st.image("images/MI.jpg", use_container_width=True)
        st.link_button("Marching Illini Website", "https://www.marchingillini.com/", use_container_width=True)
    with texts:
        st.subheader("Section Leader @ Marching Illini")
        st.markdown("*August 2022 - Present*")
        with st.container(border=True):
            st.markdown("""
                        * Tenor Drum Section Leader of the Marching Illini Drumline dedicating 18-20 weekly hours 
                        * Social Media Manager for all Illini Drumline and Illini Tenor accounts—Instagram, Facebook, TikTok 
                        * Social Coordinator for all Drumline events, and communicating with directors for extracurricular opportunities 
                        * Merch Team Manager, designing and supplying merchandise for the Illini Drumline and public
                        """)
        st.markdown(":orange-badge[Leadership] :orange-badge[Teamwork]")
    "---"
