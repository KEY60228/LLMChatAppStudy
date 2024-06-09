import streamlit as st

st.title("langchain-streamlit-app")

prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = "Hey"
        st.markdown(response)
