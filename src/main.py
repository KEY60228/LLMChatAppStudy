from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
tools = load_tools(["terminal"])
prompt = hub.pull("hwchase17/openai-tools-agent")

agent = create_openai_tools_agent(chat, tools, prompt)
agent_chain = AgentExecutor(agent=agent, tools=tools)

result = agent_chain.invoke({"input": "langchainディレクトリにあるファイルの一覧を教えて"})
print(result["output"])
