from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def translate_text(text, source_language, target_language):
    model = genai.GenerativeModel("gemini-flash-latest")
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

def main():
    st.set_page_config(page_title="AI Translator", page_icon="🌐")
    st.header("🌐 AI-Powered Language Translator")

    text = st.text_area("Enter text:")
    source_language = st.selectbox("Source Language", ["English", "Spanish", "French", "German", "Chinese"])
    target_language = st.selectbox("Target Language", ["English", "Spanish", "French", "German", "Chinese"])

    if st.button("Translate"):
        if text:
            result = translate_text(text, source_language, target_language)
            st.write(result)

if __name__ == "__main__":
    main()
