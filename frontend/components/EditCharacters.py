import streamlit as st
import pandas as pd 

def AddCharacters():
    st.session_state["Characters"].append({})
    
def EditCharacters():
    df = pd.DataFrame(st.session_state["Characters"])
    edited_df = st.data_editor(df, key='characters')
    col1, col2 = st.columns(2)
    
    with col1:
        st.button("Add Character", type="primary",on_click=AddCharacters)
    with col2:
        if st.button("Save Characters", type="primary"):
            # call save function from backend
            return