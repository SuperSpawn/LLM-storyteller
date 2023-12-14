from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

class BehindTheScenes:
    def __init__(self) -> None:
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
        self.llm = Ollama(model="llama2")
        self. runnable = self.prompt | self.llm | StrOutputParser()

    # Method that takes characters, locations and prompt and returns story (str)
    def create_story(self, characters, locations, story_prompt):
        return self.runnable.invoke({'characters': characters, 'locations': locations, 'story_prompt': story_prompt})


director = BehindTheScenes()

res = director.create_story([
    {'name': "Talal", 'age': 20, 'description': 'Young programmer'},
    {'name': "Mosab", 'age': 24, 'description': 'Brave programmer'}
    ],
    [
        {'name': "Talal's house", 'description': "The house where Talal lives"}
    ], "Mosab and Talal want to create a programming project")

print(res)






