# TransLingua: AI-Powered Multi-Language Translator

An AI-powered web application for seamless language translation using Google's Gemini AI and Streamlit.

## Features

- **AI-Powered Translation**: Uses Google Gemini Flash model for accurate translations
- **Multi-Language Support**: English, Spanish, French, German, Chinese
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- **Real-Time Translation**: Instant translation results

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

Get your API key from: https://aistudio.google.com/apikey

## Usage

Run the application:
```bash
streamlit run translang.py
```

Or:
```bash
python -m streamlit run translang.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

1. Enter text to translate in the text area
2. Select source language
3. Select target language
4. Click "Translate" button
5. View translated text

## Use Cases

- **Global Business**: Translate documents and marketing materials
- **Academic Research**: Collaborate across language barriers
- **Travel & Tourism**: Navigate foreign environments with ease

## Technologies

- Python
- Streamlit
- Google Generative AI (Gemini)
- python-dotenv

## Project Structure

```
Project/
├── translang.py       # Main application
├── requirements.txt   # Dependencies
├── .env              # API key (create this)
└── README.md         # Documentation
```
