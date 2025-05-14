import streamlit as st

st.set_page_config(page_title="Projects - Colin Bertrand", 
                   layout="wide")


st.title("Projects")
"---"

with st.container():
    st.header("Sea Turtle Tracking")
    col1, col2 = st.columns([1, 2])
    with col1:
        with st.container(border=True):
            st.subheader("Project Description")
            st.markdown("This project visualizes the migration paths of 17 juvenile loggerhead sea turtles tracked between 2002 and 2005. " \
            "Using GPS data from the OBIS-SEAMAP database, the app maps each turtle’s journey over time, calculates movement statistics "
            "(like distance, speed, and duration), and offers an interactive, animated view of their travels. Built with **Python**, **Pandas**, "
            "and **Pydeck** in **Streamlit**, the project explores how data science can bring animal migration stories to life.")
            st.markdown(":blue-badge[Data Cleaning] :blue-badge[Data Transforming] :blue-badge[Exploratory Data Analysis] :blue-badge[Interactive Visualizations] " \
            ":blue-badge[Geospatial Analysis] :blue-badge[App Development]")
        with st.container(border=True):
            st.subheader("View Full Project")
            st.markdown(" ")
            st.markdown(" ")
            cola, colb = st.columns([1, 1])
            with cola:
                st.markdown("Interactive Streamlit App:")
                st.markdown(" ")
                st.markdown(" ")
                st.markdown(" ")
                st.markdown("GitHub Repository:")
                st.markdown(" ")
                st.markdown(" ")
                st.markdown(" ")
            with colb:
                st.link_button("Streamlit", "https://seaturtletracker.streamlit.app/", use_container_width=True)
                st.markdown(" ")
                st.markdown(" ")
                st.link_button("GitHub", "https://github.com/cbertrand451/Sea-Turtle-Tracker/tree/main", use_container_width=True)

    with col2:
        st.image("images/SeaTurtleTracking.PNG", use_container_width=True)


"---"

with st.container():
    st.header("Fighting Illini Men's Basketball Database")
    st.markdown("Coming soon...")