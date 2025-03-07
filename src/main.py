import os
import json
import streamlit as st
import google.generativeai as genai  # Import Gemini library

# Load API key from config.json
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GEMINI_API_KEY = config_data["GEMINI_API_KEY"]

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # Use "gemini-1.5-pro" if needed

# Streamlit page settings
st.set_page_config(page_title="ChatSphere", page_icon="💬", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .chat-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stChatInput {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("🤖 ChatSphere")
st.sidebar.markdown("An AI-powered chatbot")
st.sidebar.markdown("---")
st.sidebar.markdown("### Features:")
st.sidebar.markdown("- Natural Language Processing 🧠")
st.sidebar.markdown("- Context-Aware Conversations 💬")
st.sidebar.markdown("- Fast & Efficient ⚡")
st.sidebar.markdown("---")

# Main chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("🧠 Chat with Mind Blowing Questions")
st.write("Your intelligent AI assistant is here to help!")

# Initialize chat session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user message
user_prompt = st.chat_input("Type your message here...")

if user_prompt:
    # Add user's message to chat history
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Get response from Gemini
    response = model.generate_content(user_prompt)
    assistant_response = response.text  # Extract response text

    # Add response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display Gemini's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

st.markdown('</div>', unsafe_allow_html=True)
