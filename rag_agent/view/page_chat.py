import streamlit as st



st.title("Chat with RAG Agent")

st.write("This page allows you to chat with the RAG Agent. You can ask questions or have a conversation with the agent, and it will respond based on its knowledge and capabilities.")

# Placeholder for chat interface
st.subheader("Chat Interface")
user_input = st.text_input("You:", key="user_input")

if st.button("Send", key="send_button"):
    if user_input:
        # Here you would typically send the user input to the RAG Agent and get a response
        # For demonstration purposes, we'll just echo the user input
        st.write(f"RAG Agent: You said '{user_input}'")
    else:
        st.warning("Please enter a message to send.")

