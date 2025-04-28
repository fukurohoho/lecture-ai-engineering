import streamlit as st

# 参考：https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps#build-a-chatgpt-like-app

st.title("困った時用のチャットスペース")
st.markdown("デモなのでAPI keyなどは設定しておらず、決まった回答のみ返します")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = "これは回答です"
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})