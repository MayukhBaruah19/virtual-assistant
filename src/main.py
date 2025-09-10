# src/main
import os
from NLU import parse_text
from dialog import handle_intent
from ASR import transcribe_file
from mic import record_audio

def repl():
    print("Assistant ready. Choose:")
    print("(t)ext  (a)udio file  (m)ic (q)uit")

    while True:
        choice = input("> ").strip().lower()
        if choice == "q":
            break

        if choice == "t":
            text = input("You: ")

        elif choice == "a":
            # Transcribe existing test.wav
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            wav_path = os.path.join(root_dir, "test.wav")
            if not os.path.exists(wav_path):
                print("Error: test.wav not found.")
                continue
            text = transcribe_file(wav_path)
            print("ASR heard:", text)

        elif choice == "m":
            # Push-to-talk mic input
            wav_path = record_audio(duration=5)  # change duration as needed
            text = transcribe_file(wav_path)
            print("ASR heard:", text)

        else:
            continue

        # Normal pipeline
        nlu = parse_text(text)
        reply = handle_intent(nlu)
        print("Assistant:", reply)

if __name__ == "__main__":
    repl()
