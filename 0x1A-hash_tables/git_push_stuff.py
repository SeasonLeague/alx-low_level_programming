#!/usr/bin/python3 


import pyttsx3
import time 
import datetime 
from git import Repo 
import sys 


espeak Initializing Jarvis

engine = pyttsx3.init("espeak")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    speak("Initializing Jarvis...")
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>12 and hour <18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")


speak(text)
wishme()


# Create a Git repository object and initialize it in the current working directory
repo = Repo()

# Stage all changes in the repository
repo.git.add('--all')

speak('Please enter a commit message for this project')

# Prompt the user for a commit message
commit_message = input("\n")

# Create a commit with the specified commit message
repo.git.commit(m=commit_message)

# Push the commit to GitHub
repo.git.push()
time.sleep(2)
sys.system("clear")
coon_2 = "Thank you for using this tool built with love from Godspower Maurice..."
print(coon_2)
speak(coon_2)





