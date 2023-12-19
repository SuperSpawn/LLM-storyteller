import streamlit as st
import pandas as pd
from frontend.components.SelectData import SelectData

def StoryForm():
    with st.form("Create a story"):
        characters, locations =  SelectData()
        prompt = st.text_input('Story prompt', placeholder="Once upon a time..." )
        submitted = st.form_submit_button("Submit")
        if submitted:
            story = st.session_state['BTS'].create_story(characters, locations, prompt)
            st.write(story)

    # st.write('The current movie title is', title)
