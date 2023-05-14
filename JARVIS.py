import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import subprocess

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
r = sr.Recognizer()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you. Please try again.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm experiencing some technical difficulties. Please try again later.")
            return ""

# Function to process user commands
def process_command(command):
    command = command.lower()

    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'play' in command and 'youtube' in command:
        video = command.replace('play', '').replace('youtube', '').strip()
        speak(f"Playing {video} on YouTube...")
        pywhatkit.playonyt(video)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)
    elif 'goodbye' in command:
        speak("Goodbye! Have a nice day!")
        exit()
    elif 'thank you' in command:
        speak("It's my duty")
        exit()
    else:
        speak("Sorry, I'm not sure how to help with that.")

# Main program loop
if __name__ == '__main__':
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()
        process_command(command)

if 'play' in command:
    print('playing')
    speak('playing')