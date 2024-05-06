from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  PromptTemplate,
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
  SystemMessagePromptTemplate.from_template("あなたは{country}料理のプロフェッショナルです。"),
  HumanMessagePromptTemplate.from_template("以下の料理のレシピを考えてください\n\n料理名: {dish}")
])

messages = chat_prompt.format_prompt(country="イギリス", dish="肉じゃが").to_messages()

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

result = chat(messages)
print(result.content)
