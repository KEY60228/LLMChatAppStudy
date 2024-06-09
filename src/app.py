import os
import streamlit as st
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
from langchain_community.callbacks import StreamlitCallbackHandler

def create_agent_chain():
    chat = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.5,
        streaming=True,
    )
    tools = load_tools(["ddg-search", "wikipedia"])
    prompt = hub.pull("hwchase17/openai-tools-agent")
    agent = create_openai_tools_agent(chat, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools)

st.title("langchain-streamlit-app")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        agent_chain = create_agent_chain()
        response = agent_chain.invoke(
            {"input": prompt},
            {"callbacks": [callback]},
        )
        st.markdown(response["output"])

    st.session_state.messages.append({"role": "assistant", "content": response})
