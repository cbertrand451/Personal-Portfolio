import streamlit as st
from Morse import morse_generator


#Set page customizations
st.set_page_config(page_title="Home - Colin Bertrand", 
                   layout="wide")

#opening resume
with open("misc_files/Colin Bertrand Resume.pdf", "rb") as pdf_file:
    PDF = pdf_file.read()

#Page Title
st.title("Hi, I'm Colin Bertrand")

#divider
"---"



#defining columns
col1, col2, col3 = st.columns([0.6, 0.1, 0.3])

#text
with col1:
    st.subheader("Nice to meet you!")
    with st.container(border=True):
        st.markdown("I'm an aspiring data scientist with a passion for turning raw data into meaningful insights and visualizations.")
        st.markdown("I am a rising Senior at the **University of Illinois Urbana-Champaign**, majoring in **Data Science + Information Science** with a minor in **Computer Science**.")
        st.markdown("I'm currently working on projects that combine **Web-Scraping**, **Machine Learning**, and **Data Visualization** to " \
                    "present stories and create some really cool tools! " \
                    "I hope to use real world data that can have a positive impact on society, and display how the power of data analysis creates helpful solutions. ")
    st.subheader("More about Me")
    with st.container(border=True):
        st.markdown("Check out some of the other pages to learn more about me and my Data Science journey!")
        st.markdown("Feel free to download my Resume below.")
    #resume download button
    st.download_button(
        label='Download Resume',
        data= PDF, 
        file_name='Colin Bertrand Resume.pdf', 
        mime= 'application/pdf'
    )

#headshot and social links
with col3:
    st.image('images/Headshot.png')
    col4, col5, col6, col7 = st.columns([1, 3, 3, 1])
    with col5:
        st.link_button('LinkedIn', 'https://www.linkedin.com/in/colin-bertrand-512138265/', use_container_width=True)
        st.image("images/linkedin.png", use_container_width=True)
    with col6:
        st.link_button("GitHub", "https://github.com/cbertrand451", use_container_width=True)
        st.image("images/github.png", use_container_width=True)


'---'


st.header('Drum Roll Please...')
st.caption("A sneak peak at my skills with a mini data showcase!")
with st.container(border=True):
    st.markdown("I'm a member of the Marching Illini Drumline here at UIUC. To integrate my passions for computer science and percussion, I made a rhythm generator.")
    st.markdown("Simply input a word, and the program will return an audio sample of the morse code rhythm of that word. You can control the tempo with the slider. " \
    "Audio will start with 4 low beeps at the selected tempo as a countoff.")
    st.markdown("**Note**: *No special characters, only letters (A-Z) and numbers (0-9)*")


input_text = st.text_input("Input text here:", "Hello world")
vals = []
for i in range(80, 155, 5):
    vals.append(i)
bpm = st.select_slider("Select a tempo (bpm):", options=vals, )
result = morse_generator(input_text, bpm)

if input_text:
    st.write(f'Generated "{input_text}" rhythm at "{bpm}" bpm:')
    st.audio(result, format='audio/wav')
