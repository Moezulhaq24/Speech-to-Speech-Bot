# Speech-to-Speech-Bot

This project is a voice-to-voice chatbot application using Whisper for audio transcription, Groq for generating responses, and gTTS for text-to-speech conversion. The application allows users to interact with the chatbot by providing audio input, which is processed to produce a spoken response.

## Features

- **Audio Transcription:** Convert spoken language in audio files to text using the Whisper model.
- **Response Generation:** Generate a text response using the Groq API.
- **Text-to-Speech:** Convert the text response back to audio using gTTS.
- **Gradio Interface:** A user-friendly interface for interacting with the chatbot.

## Requirements

- Python 3.7 or higher
- `gradio` library
- `whisper` library
- `gtts` library
- `groq` library
- API key for Groq

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/voice-to-voice-chatbot.git
   cd voice-to-voice-chatbot
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```
   groq_api_key=YOUR_GROQ_API_KEY
   ```

## Usage

1. **Run the Application:**
   ```bash
   python app.py
   ```

2. **Interact with the Chatbot:**
   - Open the provided Gradio interface in your web browser.
   - Upload an audio file or record audio directly.
   - The chatbot will process the audio, generate a response, and provide an audio file with the response.

## Code Explanation

- **`process_audio(file_path)` Function:**
  - Loads and transcribes the audio file using Whisper.
  - Generates a response using the Groq API.
  - Converts the response text to speech using gTTS.
  - Saves the response audio to a file and returns the response text and audio file path.

- **Gradio Interface:**
  - Provides an interface for users to upload audio files and receive responses.


## Acknowledgments

- **Whisper:** OpenAI's speech-to-text model.
- **Groq:** For generating text responses.
- **gTTS:** Google Text-to-Speech library.
- **Gradio:** For creating the user interface.

 
