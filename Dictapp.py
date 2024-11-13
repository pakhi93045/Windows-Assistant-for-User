import os
import pyautogui  #we can press any keyboard key through python
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id) #selecting voice
# print(voices[0])
engine.setProperty("rate",200) #rate at which it will speak

def speak(audio): #how will it speak
    engine.say(audio)
    engine.runAndWait() #wait after speaking

dictapp = {"commandprompt":"cmd", 
           "paint":"paint",
         "word":"winword", 
         "excel":"excel", 
         "chrome":"chrome",
           "vscode":"code", 
           "powerpoint":"powerpnt",
           "notepad": "notepad",
          "calculator": "calc",
       "taskmanager": "taskmgr",
    "spotify": "Spotify.exe", # Make sure to use the exact executable name
    "onenote": "onenote",
    "edge": "msedge"
           
           }

def openappweb(query):
    speak("Launching..")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("saphi", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                found = True
                break
        
        if not found:
            try:
                # Try to open any app by its name if not in dictionary
                os.startfile(query)
                speak(f"Launching {query}")
            except FileNotFoundError:
                speak("Sorry, I cannot find the application.")
                print(f"Application '{query}' not found.")


def closeappweb(query):
    speak("Closing..")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Tab closed")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Tabs closed")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Tabs closed")
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Tabs closed")
        
    elif "all tabs" in query:
        pyautogui.hotkey("ctrl", "shift", "w")
        speak("All tabs closed")    
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
    
    







