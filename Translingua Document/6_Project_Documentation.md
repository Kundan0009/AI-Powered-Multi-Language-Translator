# 6. Project Documentation

## Code Documentation

### File Structure
```
Project/
├── translang.py          # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # API key configuration
├── README.md            # Project documentation
└── Translingua Document/ # Project phase documents
```

### Main Components

#### 1. Imports and Configuration
```python
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

#### 2. Translation Function
```python
def translate_text(text, source_language, target_language):
    """
    Translates text from source language to target language using Gemini AI
    
    Args:
        text (str): Text to translate
        source_language (str): Source language name
        target_language (str): Target language name
    
    Returns:
        str: Translated text
    """
    model = genai.GenerativeModel("gemini-flash-latest")
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text
```

#### 3. Main Application
```python
def main():
    """
    Main Streamlit application function
    Sets up UI and handles user interactions
    """
    st.set_page_config(page_title="AI Translator", page_icon="🌐")
    st.header("🌐 AI-Powered Language Translator")
    
    # User inputs
    text = st.text_area("Enter text:")
    source_language = st.selectbox("Source Language", [...])
    target_language = st.selectbox("Target Language", [...])
    
    # Translation logic
    if st.button("Translate"):
        if text:
            result = translate_text(text, source_language, target_language)
            st.write(result)
```

## User Guide

### Installation
1. Install Python 3.7+
2. Install dependencies: `pip install -r requirements.txt`
3. Get API key from https://aistudio.google.com/apikey
4. Create .env file with API key

### Running the Application
```bash
streamlit run translang.py
```

### Using the Translator
1. Enter text in the text area
2. Select source language
3. Select target language
4. Click "Translate"
5. View translated result

## API Documentation

### Google Generative AI
- **Model**: gemini-flash-latest
- **Method**: generate_content()
- **Input**: Text prompt with translation instructions
- **Output**: Translated text

### Environment Variables
- `GOOGLE_API_KEY`: Google AI Studio API key

## Maintenance Guide

### Updating Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Checking Available Models
```python
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
```

### Troubleshooting
- **API Error 404**: Check model name availability
- **Authentication Error**: Verify API key in .env
- **Import Error**: Reinstall dependencies

## Future Enhancements

### Potential Features
- Add more languages
- Translation history
- File upload support
- Batch translation
- Language detection
- Audio translation
- Export translations

## Project Metrics

### Performance
- Average translation time: 2-4 seconds
- Supported languages: 5
- Maximum text length: 5000 characters

### Success Criteria
✅ Accurate translations across language pairs
✅ User-friendly interface
✅ Fast response times
✅ Stable API integration
✅ Complete documentation
