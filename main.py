from faster_whisper import WhisperModel

# from faster_whisper import WhisperModel

model = WhisperModel("small", device="cuda", compute_type="float16", local_files_only=False)


# Use GPU with float16 for speed
# model = WhisperModel("small", device="cuda", compute_type="float16")

segments, info = model.transcribe("test1.wav", beam_size=5, language="en")

print("Detected language:", info.language)
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
