import streamlit as st
import pandas as pd
from components.CharacterAndLocation import SelectData

def StoryForm():
    with st.form("my_form"):
        character,location =  SelectData()
        prompt = st.text_input('Story prompt', placeholder="Write Your Story" )
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("done",prompt,character,location)

    # st.write('The current movie title is', title)
