import streamlit as st
import google.generativeai as genai
from streamlit_mermaid import st_mermaid
import os

st.set_page_config(page_title="Module Creator", layout="wide")


st.markdown("# Module Creator")
st.sidebar.markdown("# Module Creator")

# Function to initialize Google AI
def initialize_google_ai():
    """
    Initialize the Google GenerativeAI with the provided API key.
    Returns the configured model for text generation.
    """
    # genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    genai.configure(api_key='GOOGLE_API_KEY')
    
    # Configure the model settings
    generation_config = {
        'temperature': 0.7,
        'top_p': 1,
        'top_k': 1,
        'max_output_tokens': 2048,
    }
    
    # Initialize the model
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash-001',
        generation_config=generation_config
    )
    
    return model

# Function to generate Mermaid diagram code
def generate_mermaid_code(model, prompt):
    """
    Generate Mermaid diagram code using Google's GenerativeAI.
    
    Args:
        model: The initialized Google AI model
        prompt: User's diagram request
    Returns:
        Generated Mermaid diagram code
    """
    # Enhance the prompt to specifically request Mermaid syntax
    enhanced_prompt = f"""
    Create a Mermaid diagram code for the following request: {prompt}, use Corteza field type as propery type
    
    Please provide only the Mermaid code without any markdown formatting or explanation.
    Ensure the code is valid Mermaid syntax.
    """
    
    response = model.generate_content(enhanced_prompt)
    # Extract the Mermaid code from the response
    mermaid_code = response.text.strip()
    
    # Remove any potential markdown code blocks if present
    mermaid_code = mermaid_code.replace('```mermaid', '').replace('```', '').strip()
    
    return mermaid_code

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("🎨 Mermaid Diagram Generator")
    
    # Add description
    st.write("""
    This app uses Google's Generative AI to create Mermaid diagrams based on your description.
    Simply enter your request, and the AI will generate a diagram for you!
    """)
    
    # Check for API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        st.error("Please set your GOOGLE_API_KEY environment variable")
        st.stop()
    
    try:
        # Initialize the model
        model = initialize_google_ai()
        
        # Create input area
        user_prompt = st.text_area(
            "Describe the diagram you want to create:",
            height=100,
            placeholder="Example: Create a flowchart showing the process of making coffee"
        )
        
        if st.button("Generate Diagram"):
            if user_prompt:
                with st.spinner("Generating your diagram..."):
                    try:
                        # Generate the Mermaid code
                        mermaid_code = generate_mermaid_code(model, user_prompt)
                        
                        # Display the diagram
                        st.subheader("Generated Diagram")
                        st_mermaid(mermaid_code)
                        
                        # Show the generated code
                        with st.expander("View Mermaid Code"):
                            st.code(mermaid_code, language="mermaid")
                            
                    except Exception as e:
                        st.error(f"Error generating diagram: {str(e)}")
            else:
                st.warning("Please enter a description for your diagram")
                
    except Exception as e:
        st.error(f"Error initializing the application: {str(e)}")

if __name__ == "__main__":
    main()