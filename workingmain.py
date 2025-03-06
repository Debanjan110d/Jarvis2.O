import pyttsx3
import speech_recognition as sr
import webbrowser

import time

engine = pyttsx3.init()

voices = engine.getProperty('voices')


# Sound Settings
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 125)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()  




# Voice Recognition Settings
while True:
    command = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-IN')
        command = command.lower()
        print(f"User said: {command}\n")
    except Exception as e:
        print("Unable to Recognize your voice. Please try again.")


    if "hello" in command:
        speak("Hello, I am your virtual assistant. How can I help you today?")
    elif "open youtube" in command:
        speak("Opening Youtube")
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        speak("Opening Google")
        time.sleep(1)
        webbrowser.open("https://www.google.com/")
    elif "open instagram" in command:
        speak("Opening Instagram")
        time.sleep(1)
        webbrowser.open("https://www.instagram.com/")
    elif "open twitter" in command:
        speak("Opening Twitter")
        time.sleep(1)
        webbrowser.open("https://www.twitter.com/")
    elif "open facebook" in command:
        speak("Opening Facebook")
        time.sleep(1)
        webbrowser.open("https://www.facebook.com/")
    elif "open github" in command:
        speak("Opening GitHub")
        time.sleep(1)
        webbrowser.open("https://www.github.com/")
    elif "open stackoverflow" in command:
        speak("Opening StackOverflow")
        time.sleep(1)
        webbrowser.open("https://www.stackoverflow.com/")
    