import whisper

# Load the model
model = whisper.load_model("medium")

# Transcribe an audio file
result = model.transcribe("test1.wav")

print(result["text"])
