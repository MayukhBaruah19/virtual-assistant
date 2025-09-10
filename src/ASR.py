# src/ASR.py
import os
from faster_whisper import WhisperModel

# Load tiny whisper model once
model = WhisperModel(
    r"D:\models\faster-whisper-tiny", 
    device="cuda", 
    compute_type="int8_float16"
)

def transcribe_file(wav_path: str) -> str:
    """Transcribes a wav file into text using faster-whisper."""
    segments, info = model.transcribe(wav_path, beam_size=5)
    return " ".join([s.text for s in segments]).strip()