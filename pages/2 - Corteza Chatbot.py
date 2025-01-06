import streamlit as st
import google.generativeai as genai
from google.generativeai import caching
import requests
from PIL import Image
import os
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="Corteza Assistant",
    page_icon="💬",
    layout="wide"
)

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Cache the documentation content
@st.cache_data
def load_documentation():
    url = "https://raw.githubusercontent.com/phatle96/corteza-how-to/refs/heads/main/Corteza%20docs.md"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "Failed to load documentation"

# Configure Google Generative AI
def configure_genai():
    
    docs = load_documentation()
    model_name = "gemini-1.5-flash-001"
    
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    corteza_cache = caching.CachedContent.create(
        model=model_name,
        system_instruction=f"""
            You are a helpful Corteza assistant.
            If you're not sure about something, please say so. Keep responses clear and concise.
            Always base your answers on the provided documentation.
        """,
        contents=[docs],
    )
    model = genai.GenerativeModel.from_cached_content(cached_content=corteza_cache)
    return model

# Function to generate response
def get_ai_response(prompt, model):
    
    # Combine system prompt with user's question
    full_prompt = f"User Question: {prompt}"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    st.title("🤖 Corteza Assistant")
    st.subheader("Ask me anything about Corteza!")
    
    # Set up the model
    try:
        model = configure_genai()
    except Exception as e:
        st.error(f"Error configuring Google Generative AI: {str(e)}")
        st.info("Please make sure you have set the GOOGLE_API_KEY environment variable.")
        return

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know about Corteza?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ai_response(prompt, model)
                st.write(response)
                
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()