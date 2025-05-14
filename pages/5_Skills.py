import streamlit as st

st.set_page_config(page_title="Skills - Colin Bertrand", 
                   layout="wide")


st.title("Skills")
"---"

with st.container(border=True):
    st.header("Hard Skills")
col1, col2 = st.columns([1, 3])
with col1:
    with st.container(border=True):
        st.markdown("**Programming Languages**")
    with st.container(border=True):
        st.markdown("**Libraries and Frameworks**")
    with st.container(border=True):
        st.markdown("**Programs**")
    with st.container(border=True):
        st.markdown("**Tools**")
with col2:
    with st.container(border=True):
        st.markdown(":blue-badge[Python] :blue-badge[SQL] :blue-badge[Java] :blue-badge[C++]")
    with st.container(border=True):
        st.markdown(":blue-badge[Pandas] :blue-badge[Scikit-learn] :blue-badge[NumPy] :blue-badge[Matplotlib] :blue-badge[Seaborn] :blue-badge[SciPy] :blue-badge[Plotly] :blue-badge[BeautifulSoup] " \
        ":blue-badge[Streamlit] :blue-badge[Statsmodels] :blue-badge[PyTorch] :blue-badge[Altair]")
    with st.container(border=True):
        st.markdown(":blue-badge[GitHub] :blue-badge[VSCode] :blue-badge[Cursor] :blue-badge[Excel] :blue-badge[Microsoft]")
    with st.container(border=True):
        st.markdown(":blue-badge[Machine Learning] :blue-badge[Data Visualizations] :blue-badge[Generative AI] :blue-badge[Figma]")
    
"---"
with st.container(border=True):
    st.header("Soft Skills")
col1, col2 = st.columns([1, 3])
with col1:
    with st.container(border=True):
        st.markdown("**Technical**")
    with st.container(border=True):
        st.markdown("**Traits and Experiences**")
    with st.container(border=True):
        st.markdown("**Interests**")
with col2:
    with st.container(border=True):
        st.markdown(":orange-badge[Statistics] :orange-badge[Calculus] :orange-badge[Linear Algebra] :orange-badge[Tutoring]")
    with st.container(border=True):
        st.markdown(":orange-badge[Leadership] :orange-badge[Teamwork] :orange-badge[Social Media Manager] :orange-badge[Drumline Social Chair]")
    with st.container(border=True):
        st.markdown(":orange-badge[10+ Years of Percussion] :orange-badge[Graphic Design] :orange-badge[Music Composition] :orange-badge[3D Printing]")

    