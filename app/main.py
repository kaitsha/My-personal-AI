from fastapi import FastAPI
from app.utils import chat, stt, tts

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello my dear! I'm ready to help you!"}

@app.post("/chat")
def chat_with_ai(prompt: str):
    return {"response": chat.get_ai_response(prompt)}

@app.post("/speech-to-text")
def speech_to_text(audio_path: str):
    return {"text": stt.transcribe_audio(audio_path)}

@app.post("/text-to-speech")
def text_to_speech(text: str):
    tts.speak(text)
    return {"status": "Speaking now!"}
