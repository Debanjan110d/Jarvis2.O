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
    

#Song Searching capability
def search_song(song_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'default_search': 'ytsearch5',  # Search for top 5 results
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(song_name, download=False)
        if 'entries' in info:
            results = [(entry['title'], entry['url']) for entry in info['entries']]
            return results
    return None

def play_audio(url):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    player.set_media(media)
    player.play()
    
    print("Playing song...")
    time.sleep(2)  # Wait for player to start
    while player.is_playing():
        time.sleep(1)  # Keep running while song plays

def play_music():
    speak("Which song would you like to play?")
    song_name = listen()
    if not song_name:
        return

    speak(f"Searching for {song_name}...")
    results = search_song(song_name)
    
    if not results:
        speak("No results found.")
        return

    for i, (title, _) in enumerate(results, start=1):
        print(f"{i}. {title}")
        speak(f"Option {i}: {title}")

    speak("Please say the number of the song you want to play.")
    choice = listen()

    if choice and choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(results):
            _, url = results[index]
            speak("Playing your selected song.")
            play_audio(url)
        else:
            speak("Invalid choice.")
    else:
        speak("Could not understand your selection.")

if __name__ == "__main__":
    while True:
        print("Say 'play music' to start.")
        command = listen()
        if command and "play music" in command:
            play_music()