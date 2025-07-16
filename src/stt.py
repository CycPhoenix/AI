import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:\
        print("Please say something:")
        audio = recognizer.listen(source)
    
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not requirest results; check your network connection.")

if __name__ == "__main__":
    recognize_speech()