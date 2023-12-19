import streamlit as st


def getName(obj):
    return obj["name"] 

def SelectData():
        charactersOptions = st.multiselect(
            'Choose Character',
            st.session_state["Characters"],
            format_func=getName
        )
        locationsOptions = st.multiselect(
            'Choose Location',
            st.session_state["Locations"],
            format_func=getName
        )
        return (charactersOptions, locationsOptions)
