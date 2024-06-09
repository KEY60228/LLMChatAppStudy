import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

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
        chat = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.5,
        )
        messages = [HumanMessage(content=prompt)]
        response = chat(messages)
        st.markdown(response.content)

    st.session_state.messages.append({"role": "assistant", "content": response})
