import streamlit as st
from backend.BTS import BTS
from langchain.llms import Ollama

def reset():
    if 'BTS' not in st.session_state:
        llm = Ollama(model='llama2')
        st.session_state['BTS'] = BTS(llm)



