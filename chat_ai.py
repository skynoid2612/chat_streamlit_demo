import streamlit as st
from gpt4all import GPT4All
# import openai

# Set up your OpenAI API credentials
# openai.api_key = 'YOUR_API_KEY'

# Title of the Streamlit app
model = GPT4All(model_name='orca-mini-13b.ggmlv3.q4_0.bin')
# Initialize conversation history
conversation_history = []
st.title("ChatGPT Demo")
# Main chat loop
with model.chat_session():
    # User input
    user_input = st.text_input("User:", "")

    # Add user input to conversation history
    conversation_history.append(f"User: {user_input}")

    # Generate model response
    model_reply = model.generate(prompt=user_input, top_k=2000)

    # Get model's reply
    # model_reply = response.choices[0].text.strip()

    # Add model reply to conversation history
    conversation_history.append(f"AI: {model_reply.encode('utf-8').decode('unicode_escape')}")

    # Display model's reply
    st.text_area("AI:", model_reply, key='output')

    # Clear conversation history if user inputs '/clear'
    if user_input.strip() == '/clear':
        conversation_history = []
