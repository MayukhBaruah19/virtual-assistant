# src/mic.py
import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="mic_input.wav", duration=10, samplerate=16000):
    """
    Records audio from default mic for given duration.
    Saves it as a wav file and returns the file path.
    """
    print(f"[Mic] Recording for {duration} seconds... Speak now!")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
    sd.wait()  # Wait until recording is finished
    write(filename, samplerate, recording)
    print(f"[Mic] Saved to {filename}")
    return os.path.abspath(filename)
