# src/dialog.py
from skills import set_timer, control_light

SKILLS = {
    "set_timer": set_timer,
    "control_light": control_light,
}

def handle_intent(nlu_res):
    intent = nlu_res["intent"]
    slots = nlu_res.get("slots", {})
    fn = SKILLS.get(intent)
    if not fn:
        return "Sorry, I can't do that yet."
    return fn(**slots)


