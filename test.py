import sounddevice as sd
from scipy.io.wavfile import write

def test_mic(device_index=1, duration=5, samplerate=16000, filename="mic_test.wav"):
    sd.default.device = (device_index, None)  # (input, output)
    print(f"[Mic] Recording from device {device_index} for {duration} seconds... Speak now!")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
    sd.wait()
    write(filename, samplerate, recording)
    print(f"[Mic] Saved to {filename}")

if __name__ == "__main__":
    # Try 1, then if silent, try 6, then 12
    test_mic(device_index=1)
