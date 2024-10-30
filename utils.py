import pyttsx3

def narrate_text(text):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set speech rate
    engine.setProperty('rate', 150)

    # Narrate text
    engine.say(text)
    engine.runAndWait()