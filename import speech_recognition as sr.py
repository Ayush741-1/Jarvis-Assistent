import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)

# Adjust the speech rate (you can experiment with different values)
engine.setProperty('rate', 140)  # Adjust this value to control the speed

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.WaitTimeoutError:
            print("Timeout. Please try again.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    command = listen()

    if command:
        if "hello" in command.lower():
            speak("Hello! How can I help you?")
        elif "goodbye" in command.lower():
            speak("Goodbye!")
            break
        else:
            try:
                result = wikipedia.summary(command, sentences=3)
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                print("There are multiple possible matches. Please be more specific.")
                speak("There are multiple possible matches. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                print("I couldn't find any information on that topic.")
                speak("I couldn't find any information on that topic.")
