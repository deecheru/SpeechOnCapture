from gtts import gTTS


def text_to_speech(text):
    """
    Convert text to speech and speak it in real-time.

    :param text: The text to convert to speech and speak.

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()"""
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")





# Create a gTTS object


# Save the generated speech to an MP3 file
