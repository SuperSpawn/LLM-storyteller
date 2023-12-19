import streamlit as st   
import pandas as pd 


from backend.config.data import get_characters
from backend.config.data import get_locations

def reset():
    if "Locations" not in st.session_state:
        st.session_state["Locations"] = get_locations()
    if "Characters" not in st.session_state:    
        st.session_state["Characters"] = get_characters()