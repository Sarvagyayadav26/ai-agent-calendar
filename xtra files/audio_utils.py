import speech_recognition as sr
import pyttsx3

def text_to_audio(text):
    """Convert text to speech and play the audio."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def audio_to_text():
    """Listen from microphone and convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
