import streamlit as st

st.set_page_config(page_title="Extracurriculars and Hobbies - Colin Bertrand", 
                   layout="wide")


st.title("Extracurriculars and Hobbies")
"---"

with st.container():
    pic1, text1 = st.columns([1, 1])
    with pic1:
        st.image("images/IDL_gp.jpg")
    with text1:
        st.header("Illini Drumline", divider="orange")
        st.markdown("*May 2022 - Present*")
        with st.container(border=True):
            st.markdown("""
                        * 4 Years on the Illini Drumline playing tenors, finishing as Section Leader
                        * Performing at a multitude of events relating to Illini Athletics
                        * Providing entertainment and "hype" for fans
                        * Forming bonds with the other members of the drumline
                        """)
        st.link_button("Illini Drumline Instagram", "https://www.instagram.com/illinidrumline/", use_container_width=True)
        st.link_button("Illini Drumline Info", "https://www.marchingillini.com/about-us/illini-drumline-2", use_container_width=True)

with st.container():
    text1, pic1 = st.columns([1, 1])
    with pic1:
        st.image("images/BBallBand.JPG")
    with text1:
        st.header("Men's Basketball Band", divider="blue")
        st.markdown("*Sept 2024 - Present*")
        with st.container(border=True):
            st.markdown("""
                        * Drumset player for the Men's Fighting Illini Basketball Team
                        * Performing at a home basketball games
                        * Requires initiative and self-reliance
                        """)
        st.link_button("Basketball Band Instagram", "https://www.instagram.com/marchingillini/", use_container_width=True)
        st.link_button("Basketball Band Info", "https://www.marchingillini.com/join/ensembles/athletic-bands/basketball-bands", use_container_width=True)

with st.container():
    pic1, text1 = st.columns([1, 1])
    with pic1:
        st.image("images/foil_board.JPG")
    with text1:
        st.header("eFoiling", divider="orange")
        with st.container(border=True):
            st.markdown("""
                        * Water sport that uses an electric hydrofoil to propel a board above the water
                        * Usually eFoiling on the east beaches of Lake Michigan
                        * Less fuel/energy consumption than even a surfboard style because it's more hydrodynamic. 
                        Less noise leads to smaller waves and impact to shorelines, other boats, and marinas
                        """)
        st.link_button("What is an eFoil?", "https://waydoo.com/blogs/learn-more-about-efoil/what-is-an-efoil-how-much-does-one-cost#:~:text=The%20eFoil%20board(or%20Electric,Waydoo%20Flyer%20One%20eFoil%20board)", use_container_width=True)
        st.link_button("eFoiling Video", "https://www.youtube.com/watch?v=fShrScFKLcY", use_container_width=True)

with st.container():
    text1, pic1 = st.columns([1, 1])
    with pic1:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.image("images/Chicken_Vintage.png", use_container_width=True)
        with col2:
            st.image("images/BowlGameFirst.png", use_container_width=True)
        with col3:
            st.image("images\Poster.png", use_container_width=True)
    with text1:
        st.header("Photoshop", divider="violet")
        with st.container(border=True):
            st.markdown("""
                        * Create's high quality graphics for Illini Drumline social media accounts
                        * Use Adobe Photoshop for all projects
                        """)