# src/nlu.py
import re

def parse_text(text: str):
    t = text.lower().strip()
    # simple timer rule
    m = re.search(r"(\d+)\s*(sec|second|s|minute|min|m)s?", t)
    if "timer" in t or m:
        if m:
            val = int(m.group(1))
            if 'min' in m.group(2):
                seconds = val * 60
            else:
                seconds = val
        else:
            seconds = 60
        return {"intent":"set_timer","slots":{"duration_seconds": seconds}, "confidence": 0.8}
    if "turn" in t or "switch" in t:
        state = "on" if "on" in t else "off"
        return {"intent":"control_light", "slots":{"device":"light","state":state}, "confidence":0.7}
    return {"intent":"chitchat","slots":{}, "confidence":0.3}
