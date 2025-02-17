import streamlit as st
import openai

# Set OpenAI API key (Replace with your own)
openai.api_key = "your_openai_api_key"

# Function to analyze Python code
def analyze_code(user_code):
    prompt = f"Analyze the following Python code for bugs and suggest fixes:\n\n{user_code}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("GenAI App - AI Code Reviewer")
st.write("Submit your Python code for AI-powered bug detection and fixes.")

# User input section
user_code = st.text_area("Paste your Python code here:", height=200)

# Analyze button
if st.button("Analyze Code"):
    if user_code.strip():
        st.subheader("Bug Analysis & Suggested Fixes")
        result = analyze_code(user_code)
        st.code(result, language="python")
        
        # Download button for fixed code
        st.download_button("Download Fixed Code", result, file_name="fixed_code.py", mime="text/plain")
    else:
        st.warning("Please enter some Python code first.")

# Run the app using: streamlit run app.py
