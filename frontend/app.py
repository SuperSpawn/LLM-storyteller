import streamlit as st
import pandas as pd
from components.EditCharacters import EditCharacters
from components.EditLoactions import EditLocations
from config.reset import reset
from components.StoryForm import StoryForm
reset()

StoryForm()
EditCharacters()
# if "x" not in st.session_state:
#     st.session_state["x"] = 5
    

# if st.button("add"):
#     st.session_state["x"]+=1
# st.write(st.session_state["x"])    