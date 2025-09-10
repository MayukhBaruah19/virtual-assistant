# src/skills.py
import threading, time

def set_timer(duration_seconds: int):
    def ring():
        time.sleep(duration_seconds)
        print("[TIMER] Ding! Timer finished.")
    threading.Thread(target=ring, daemon=True).start()
    return f"Timer set for {duration_seconds} seconds."

def control_light(device: str, state: str, room: str | None = None):
    # placeholder for MQTT / REST call
    return f"{device} turned {state}" + (f" in {room}." if room else ".")
