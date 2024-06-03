from langchain_core.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)

from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
tools = load_tools(["ddg-search"])
prompt = hub.pull("hwchase17/openai-tools-agent")

agent = create_openai_tools_agent(chat, tools, prompt)
agent_chain = AgentExecutor(agent=agent, tools=tools)

result = agent_chain.invoke({"input": "東京と大阪の天気を教えて"})
print(result["output"])
