import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"user said: {text}")
        return text
    except sr.UnknownValueError:
        return "sorry, could not understand audio."
