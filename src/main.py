from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent, load_tools

summarize_prompt = PromptTemplate.from_template("""以下の文章を結論だけ一言に要約してください。

{input}
"""
)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
prompt = hub.pull("hwchase17/react")

summarize_chain = (
  {"input": RunnablePassthrough()}
  | summarize_prompt
  | model
  | StrOutputParser()
)

tools = [
  Tool.from_function(
    func=summarize_chain.invoke,
    name="Summarizer",
    description="Text summarizer",
  )
]

agent = create_react_agent(model, tools, prompt)
agent_chain = AgentExecutor(agent=agent, tools=tools)

text = """以下を要約してください。
ChatGPT（チャットジーピーティー、英語: Chat Generative Pre-trained Transformer）[1]は、OpenAIが2022年11月に公開した人工知能チャットボットであり、生成AIの一種。GPTの原語のGenerative Pre-trained Transformerとは、「生成可能な事前学習済み変換器」という意味である[2]。OpenAIのGPT-3ファミリーの大規模な言語モデルに基づいて構築されており、教師あり学習と強化学習の両方の手法を使って転移学習され、機械学習のサブセットである深層学習を使って開発されている
"""

result = agent_chain.invoke({"input": text})
print(result["output"])
