import os
import gradio as gr
import whisper
from gtts import gTTS
import io
from groq import Groq

Groq_Api_Key = os.getenv("groq_api_key")
# Initialize the Groq client
client = Groq(api_key=Groq_Api_Key)

# Load the Whisper model
model = whisper.load_model("base")  # You can choose other models like "small", "medium", "large"

def process_audio(file_path):
    try:
        # Load the audio file
        audio = whisper.load_audio(file_path)

        # Transcribe the audio using Whisper
        result = model.transcribe(audio)
        text = result["text"]

        # Generate a response using Groq
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": text}],
            model="llama3-8b-8192",  # Replace with the correct model if necessary
        )

        # Access the response using dot notation
        response_message = chat_completion.choices[0].message.content.strip()

        # Convert the response text to speech
        tts = gTTS(response_message)
        response_audio_io = io.BytesIO()
        tts.write_to_fp(response_audio_io)  # Save the audio to the BytesIO object
        response_audio_io.seek(0)

        # Save audio to a file to ensure it's generated correctly
        with open("response.mp3", "wb") as audio_file:
            audio_file.write(response_audio_io.getvalue())

        # Return the response text and the path to the saved audio file
        return response_message, "response.mp3"

    except Exception as e:
        return f"An error occurred: {e}", None

iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath"),  # Use type="filepath"
    outputs=[gr.Textbox(label="Response Text"), gr.Audio(label="Response Audio")],
    live=True,
    title="Voice-to-Voice Chatbot"
)

iface.launch()
