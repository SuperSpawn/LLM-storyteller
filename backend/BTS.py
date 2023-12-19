from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

class BTS:
    def __init__(self, llm) -> None:
        self.prompt = PromptTemplate.from_template(
            """you are an LLM tasked with writing stories.
            Given a set of characters, locations and a story prompt you must write a great story.
            Characters:
            {characters}
            Locations:
            {locations}
            Story prompt: {story_prompt}
            Response:"""
        )
        self.llm = llm
        self. runnable = self.prompt | self.llm | StrOutputParser()

    # Method that takes characters, locations and prompt and returns story (str)
    def create_story(self, characters, locations, story_prompt):
        return self.runnable.invoke({'characters': characters, 'locations': locations, 'story_prompt': story_prompt})








