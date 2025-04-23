from detect_user import is_user_present
from calendar_gaps import get_calendar_event
from gemma_run import run_gemma
from play_audio import speak
from record_audio import transcribe_audio
from datetime import datetime

def log_conversation(event_type, transcript, response):
    with open("logs/session_log.txt", "a") as log:
        log.write(f"\n[{datetime.now()}] EVENT: {event_type.upper()}\nUSER: {transcript}\nGEMMA: {response}\n")

event_map = {
    "commute": "prompts/commute.txt",
    "church": "prompts/church.txt",
    "gap": "prompts/journal.txt"
}

if is_user_present():
    event_type = get_calendar_event()
    if event_type in event_map:
        response = run_gemma(event_map[event_type])
        speak(response)
        user_input = transcribe_audio()
        log_conversation(event_type, user_input, response)
