import streamlit as st
import import_ipynb
import youtube
import textwrap

st.title("My own YouTube Assistant")

with st.sidebar:
    with st.form(key = 'my_form'):
        youtube_url = st.sidebar.text_area(
            label = "Enter the YouTube video url",
            max_chars = 50
        )
        question = st.sidebar.text_area(
            label = "What question do you have in your mind?",
            max_chars = 100
        )

        submit_button = st.form_submit_button(label = "Submit")

if question and youtube_url:
    db = youtube.vectordb_from_youtube(youtube_url)
    response =youtube.get_response(db, question)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width = 80))
        


