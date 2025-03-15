import os
import uuid
from gtts import gTTS

def speak(text: str) -> str:
    """
    Convert text to speech using gTTS, store mp3 in app/audio folder.
    Returns the file path of the generated audio.
    """
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    audio_dir = "app/audio"
    os.makedirs(audio_dir, exist_ok=True)
    filepath = os.path.join(audio_dir, filename)

    tts = gTTS(text)
    tts.save(filepath)
    return filepath
