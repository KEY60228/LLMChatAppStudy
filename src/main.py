from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Recipe(BaseModel):
  ingredients: list[str] = Field(description="ingredients of the dish")
  steps: list[str] = Field(description="steps to make the dish")

parser = PydanticOutputParser(pydantic_object=Recipe)

template = """料理のレシピを考えてください。

{format_instructions}

料理名: {dish}
"""

prompt = PromptTemplate(
  template=template,
  input_variables=["dish"],
  partial_variables={"format_instructions": parser.get_format_instructions()},
)

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain = LLMChain(prompt=prompt, llm=chat, output_parser=parser)

recipe = chain.run(dish="カレー")

print(type(recipe))
print(recipe)
