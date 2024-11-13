import pyautogui
import time
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Speed of speech

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=90)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}")
        return query
    except Exception as e:
        print("Could not understand. Please try again.")
        return None

# Function to open WhatsApp and send a message
def sendMessage():
    # Open WhatsApp desktop app
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('WhatsApp')
    time.sleep(1)
    pyautogui.press('enter')
    
    time.sleep(5)  # Wait for WhatsApp to fully load

    # Ask for the contact name
    speak("Who would you like to message?")
    contact_name = takeCommand()
    
    if contact_name is None:  # If speech recognition fails
        contact_name = input("Enter contact name: ")

    # Type the contact's name in the search bar (cursor is automatically in the search bar)
    pyautogui.write(contact_name)
    time.sleep(2)  # Wait for search results to load
    
    # Select the first contact by pressing down and enter
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('enter')
    
    time.sleep(2)  # Wait for the chat window to open

    # Ask for the message
    speak("What message would you like to send?")
    message = takeCommand()
    
    if message is None:  # If speech recognition fails
        message = input("Enter the message: ")

    # Type and send the message (the cursor is automatically in the message box)
    pyautogui.write(message)
    pyautogui.press('enter')

    speak("Your message has been sent.")

# Run the function
sendMessage()
