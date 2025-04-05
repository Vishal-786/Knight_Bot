import streamlit as st
import requests

#connect with LLM Model
# import requests


def chat_with_llama(user_input):
    headers = {
        "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a chess expert. Only answer chess-related questions."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]


st.set_page_config(page_title="♟️KnightBot",layout="centered")
st.title("♟️ KnightBot ")

# Initialize chat history once
if "messages" not in st.session_state:
    st.session_state.messages = []

# Print all Previous Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# user_input
user_input = st.chat_input("Type your chess question here...")

#  Once user enters input
if user_input:
    
    # store  user_input
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("User"):
        st.markdown(user_input)

    with st.spinner("Wait, Let me Think..."):
        response = chat_with_llama(user_input)
    
    #store user_response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("Assistant"):
        st.markdown(response)
