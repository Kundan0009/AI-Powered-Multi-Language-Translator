# 3. Project Design Phase

## System Architecture

### Three-Tier Architecture
1. **Presentation Layer**: Streamlit web interface
2. **Application Layer**: Python translation logic
3. **Data Layer**: Google Gemini AI API

## Component Design

### Frontend Components
- Text input area
- Source language dropdown
- Target language dropdown
- Translate button
- Result display area

### Backend Components
- API configuration module
- Translation function
- Error handling
- Response processing

## Data Flow

```
User Input → Streamlit UI → translate_text() → Gemini AI API → Response → Display
```

### Detailed Flow
1. User enters text and selects languages
2. Streamlit captures input
3. translate_text() function called
4. Prompt constructed with source/target languages
5. Request sent to Gemini AI
6. AI processes and returns translation
7. Result displayed to user

## Technology Stack

### Frontend
- Streamlit (Web UI framework)

### Backend
- Python 3.x
- google-generativeai library

### AI Model
- Google Gemini Flash (gemini-flash-latest)

### Configuration
- python-dotenv (Environment variables)

## Interface Design

### UI Elements
- Header: "🌐 AI-Powered Language Translator"
- Text Area: Multi-line input field
- Dropdowns: Language selection (2)
- Button: "Translate" action button
- Output: Translated text display
