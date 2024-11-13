import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id) #selecting voice
# print(voices[0])k
engine.setProperty("rate",200) #rate at which it will speak

def speak(audio): #how will it speak
    engine.say(audio)
    engine.runAndWait() #wait after speaking

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening") 
    #speak("greetings")
    speak("Greetings, adventurer! I'm Saphi, your AI sidekick, ready to explore the digital realm with you. Let's make magic happen—what shall we conquer today?")
