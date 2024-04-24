import pyttsx3

# Create a TTS engine
engine = pyttsx3.init()

# Function to speak the given text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()
