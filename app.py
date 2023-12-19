import streamlit as st

from frontend.config.reset import reset as frontend_reset
from frontend.components.EditCharacters import EditCharacters
from frontend.components.EditLoctions import EditLocations
from frontend.components.StoryForm import StoryForm

from backend.config.reset import reset as backend_reset


frontend_reset()
backend_reset()



EditCharacters()
EditLocations()

StoryForm()




