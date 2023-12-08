import speech_recognition as sr
#from word2number import w2n


def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        #print("Say something...")
        audio = recognizer.listen(source)


    try:
        # Use the Google Web Speech API for recognition
        text = recognizer.recognize_google(audio)
        print(text)
        #return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        text = ""
    except sr.RequestError as e:
        print("Error with the speech recognition service; {0}".format(e))
        text = ""
    return text

'''def speech_recognition_number():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 1000
    number = 0
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio)
        print(text)

        # Convert recognized text to an integer using word2number
        number = w2n.word_to_num(text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the recognition service; {e}")
    except ValueError:
        print("Unable to convert the recognized text to a number")
    return number'''


