from langchain_core.globals import set_verbose

set_verbose(True)

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
tools = load_tools(["terminal"])
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(chat, tools, prompt)

agent_chain = AgentExecutor(agent=agent, tools=tools)

result = agent_chain.invoke({"input": "langchainディレクトリにあるファイルの一覧を教えて"})
print(result["output"])
