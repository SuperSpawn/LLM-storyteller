import streamlit as st

def EditLocations(locations):
    edited_df = st.data_editor(locations)
    if st.button("save", type="primary"):
        # call save function from backend
        return


