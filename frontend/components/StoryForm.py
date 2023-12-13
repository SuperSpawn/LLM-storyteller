import streamlit as st
import pandas as pd

def getName(obj):
    return obj["Name"] 


def StoryForm():
    characters = st.session_state["Characters"]
    options = st.multiselect(
    'Choose Character',
    characters,format_func=getName
    )
    st.write('You selected:', options)

    locations = st.session_state["Locations"]
    options = st.multiselect(
    'Choose Location',
    locations,format_func=getName
    )
    st.write('You selected:', options)
