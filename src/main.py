from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

messages = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="こんにちは！私はジョンです。"),
  AIMessage(content="こんにちは、ジョンさん！どのようにお手伝いできますか？"),
  HumanMessage(content="私の名前が分かりますか？"),
]

result = chat(messages)
print(result.content)
