import streamlit as st
import pandas as pd 

def AddLocation():
    st.session_state["Locations"].append({})
    
def EditLocations():
    df = pd.DataFrame(st.session_state["Locations"])
    edited_df = st.data_editor(df, key='locations')
    col1, col2 = st.columns(2)
    
    with col1:
        st.button("Add Location", type="primary",on_click=AddLocation)
    with col2:
        if st.button("Save Locations", type="primary"):
            # call save function from backend
            st.session_state['Locations'] = edited_df
            