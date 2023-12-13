import streamlit as st   
import pandas as pd 
def reset():
    df = [
       {"Name": "st.selectbox", "Age": 4, "Description": "hello"},
       {"Name": "st.balloons", "Age": 5, "Description": "hello"},
       {"Name": "st.time_input", "Age": 3, "Description": "hello"},
       
   ]

    if "Locations" not in st.session_state:
        st.session_state["Locations"] = df
    if "Characters" not in st.session_state:    
        st.session_state["Characters"] = df