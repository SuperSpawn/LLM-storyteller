import streamlit as st
def getName(obj):
    return obj["Name"] 

def SelectData():
        characters = st.session_state["Characters"]
        charactersOptions = st.multiselect(
        'Choose Character',
        characters,format_func=getName
        )
        # st.write('You selected:', options)
        locations = st.session_state["Locations"]
        locationsOptions = st.multiselect(
        'Choose Location',
        locations,format_func=getName
        )
        return(charactersOptions,locationsOptions)
