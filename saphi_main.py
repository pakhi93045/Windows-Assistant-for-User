import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import time
import speedtest 
from speedtest import Speedtest
import pyjokes
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import instaloader
from pypdf import PdfReader
import PyPDF2
import screen_brightness_control as sbc
#Password protection

for i in range(3): #it will give 3 chances to the user
    a = input("Enter Password to open Saphi :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id) #selecting voice
# print(voices[0])
engine.setProperty("rate",200) #rate at which it will speak

def speak(audio): #how will it speak
    engine.say(audio)
    engine.runAndWait() #wait after speaking

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300 #the threshold we are speaking and it can listen too. if we put threshold as high we have to shout for it to listen and if low then it will hear the background sound as well
        audio = r.listen(source,0,4) #it will wait for 4 sec and move

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query



#pdf reader

def pdf_reader():
    try:
        # Prompt the user to enter the PDF file path
        pdf_path = input("Please enter the full path to the PDF file: ").strip()
        book = open(pdf_path, 'rb')  # Open the PDF file from the specified path

        pdfReader = PyPDF2.PdfReader(book)  # Use PdfReader to read the PDF
        pages = len(pdfReader.pages)  # Get the total number of pages
        speak(f"Total number of pages in this book are {pages}")

        # Ask user which page to read
        speak("Please enter the page number I have to read")
        pg = int(input("Please enter the page number: "))
        
        # Check if the page number is valid
        if pg < 1 or pg > pages:
            speak(f"Invalid page number. Please enter a number between 1 and {pages}")
            return

        # Extract and read the text from the selected page
        page = pdfReader.pages[pg - 1]  # Adjusting for zero-based indexing
        text = page.extract_text()
        speak(text)

    except FileNotFoundError:
        speak("The specified PDF file was not found. Please check the file path.")
    except Exception as e:
        speak(f"An error occurred: {e}")

#brightness

def increase_brightness():
    try:
        current_brightness = sbc.get_brightness()  # Get the current brightness level
        new_brightness = min(current_brightness[0] + 10, 100)  # Increase by 10%, max is 100%
        sbc.set_brightness(new_brightness)  # Set the new brightness level
        print(f"Brightness increased to {new_brightness}%")
    except Exception as e:
        print(f"Error increasing brightness: {e}")

# Function to decrease brightness
def decrease_brightness():
    try:
        current_brightness = sbc.get_brightness()  # Get the current brightness level
        new_brightness = max(current_brightness[0] - 10, 0)  # Decrease by 10%, min is 0%
        sbc.set_brightness(new_brightness)  # Set the new brightness level
        print(f"Brightness decreased to {new_brightness}%")
    except Exception as e:
        print(f"Error decreasing brightness: {e}")

#notepad
def save_notepad():
    pyautogui.hotkey("ctrl", "s")  # Save shortcut
    time.sleep(1)
    
    # Type the file path where you want to save the file
    pyautogui.typewrite(os.path.expanduser("~/Documents/saphiNotepad.txt"))
    pyautogui.press("enter")  # Press 'Enter' to save the file
    time.sleep(1)
    pyautogui.hotkey("alt", "f4")  # Close Notepad after saving
    speak("Your note has been saved successfully.")

def open_notepad():
    pyautogui.press("super")  # Opens the Start menu
    pyautogui.typewrite("notepad")
    time.sleep(2)
    pyautogui.press("enter")  # Opens Notepad
    time.sleep(2)

    speak("Do you want to use Notepad to write something? Say 'yes' or 'no'.")
    query = takeCommand()

    if "yes" in query:
        speak("Please start dictating. Say 'close notepad' when you're done.")
        
        while True:
            text = takeCommand()
            if "close notepad" in text:
                speak("Do you want to save your note? Say 'yes' to save, 'no' to discard.")
                save_response = takeCommand()



                if "yes" in save_response:
                    save_notepad()
                else:
                    pyautogui.hotkey("alt", "f4")  # Close Notepad without saving
                    pyautogui.press("n")  # Press 'N' for not saving changes
                break
            else:
                pyautogui.typewrite(text)  # Types the spoken words into Notepad

#main

if __name__ == "__main__":
    while  True:
        query = takeCommand().lower()
        #greet function
        if "wake up" in query:
            from greet import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if"go to sleep" in query:
                    speak("Slipping into stealth mode... I'll be quietly recharging. Call me when it's time for the next adventure!")
                    break

                #password change
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done")
                    speak(f"Your new password is{new_pw}")

 #scheduling the day
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()  
                        speak("Your tasks have been scheduled.")    
                    
                elif "increase brightness" in query:
                    increase_brightness()  # Call the function to increase brightness
                elif "decrease brightness" in query:
                    decrease_brightness()  # Call the function to decrease brightness



 #show schedule
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    while mixer.music.get_busy():
                        time.sleep(1) 
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                     ) 
                     
                    print(
                       content
                     ) 


 #whatsapp
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
#focus mode1
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\Pragya Pakhi\\Desktop\\saphi\\FocusMode.py")
                        exit()

                    
                    else:
                        pass                             
#open any app
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("saphi","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  

                    if "notepad" in query: 
                        open_notepad()                   

#internet speed
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print(f"Wifi Upload Speed is {upload_net:.2f} Mbps")
                    print(f"Wifi Download Speed is {download_net:.2f} Mbps")
                    speak(f"Wifi download speed is {download_net:.2f} Mbps")
                    speak(f"Wifi upload speed is {upload_net:.2f} Mbps")

#screenshot function         
                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save(r"C:\\Users\\Pragya Pakhi\\Pictures\Screenshots\ss.jpg") 

 #camera
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")    

#read pdf
                elif "read pdf" in query:
                    pdf_reader()

#hide files and folder
                elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
                    speak("Do you want to hide this folder or make it visible for everyone")
                    condition = takeCommand().lower()
                    if "hide" in condition:
                        speak("Please provide the full path of the file or folder you want to hide.")
                        file_path = input("Please enter the full path of the file or folder you want to hide: ")
  # Capture the file path input from the user
                        os.system(f'attrib +h "{file_path}"')
                        speak(f"The file or folder is now hidden.")
                        speak("All the files are now hidden.")
                    elif "visible" in condition:
                       speak("Making all hidden files visible.")
                       os.system("attrib -h /s /d")  # Unhide all files and folders
                       speak("All hidden files are now visible to everyone.")
                    elif "leave it" in condition or "leave for now" in condition:
                        speak("Ok")            
           
#greetings 
                elif "hello" in query:
                    speak("Hello, How are you? I am Saphi Let’s dive in—what's on your mind?")
                elif "i am fine" in query:
                    speak("that's great")
                elif "how are you" in query:
                    speak("I am perfect")
                elif "thank you" in query:
                    speak("You're welcome") 
#playlist
                elif "tired" in query:
                    speak("Playing your favourite songs")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=PqFMFVcCZgI")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=tgVYh94QH8k")  
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=mH_LFkWxpI0")     

#jokes
                elif "tell me a joke" in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)

#switch window
                elif "switch the window" in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")  

#email to --
                
                elif "email to sumit" in query:
                    speak("Do You want to send a file: ")
                    query = takeCommand().lower()
                    
                    if "yes" in query:
                        email= 'pragya93045@gmail.com'
                        password = 'xutr tfer qrco ihpg'
                        send_to_email = 'sklegacy789@gmail.com'
                        speak("What is the subject for this email")
                        query = takeCommand().lower()
                        subject = query
                        speak("What is the message for this email")
                        query2 = takeCommand().lower()
                        message = query2
                        speak("Please enter the correct path of the file into the shell")
                        file_location = input("Please enter the path here: ")

                        speak("Please wait, I am sending email now")

                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = send_to_email
                        msg['Subject'] = subject

                        msg.attach(MIMEText(message, 'plain'))

                        #setup the attachment
                        filename = os.path.basename(file_location)
                        attachment = open(file_location, "rb")
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment; filename= %s" %filename)


                        #attach the attachment to the MIMEMultipart object
                        msg.attach(part)

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        text = msg.as_string()
                        server.sendmail(email, send_to_email, text)
                        server.quit()
                        speak("Email has been sent")
                   
                    if "no" in query:
                        email= 'pragya93045@gmail.com'
                        password = 'xutr tfer qrco ihpg'
                        send_to_email = 'sklegacy789@gmail.com'
                        speak("What is the subject for this email")
                        query = takeCommand().lower()
                        subject = query
                        speak("What is the message for this email")
                        query2 = takeCommand().lower()
                        message = query2
                        #message = query

                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = send_to_email
                        msg['Subject'] = subject

                          # Attach the message body to the email
                        msg.attach(MIMEText(message, 'plain'))

                   # Send the email
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        text = msg.as_string()
                        server.sendmail(email, send_to_email, text)
                        server.quit()
                        speak("Email has been sent")






                    

 #youtube controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted") 

                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")     

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()              


#to open apps


                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)    









                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia 
                    searchWikipedia(query)

#news function
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()      
#calculator
                elif"calculate" in query:
                      from Calculatenumbers import WolfRamAlpha
                      from Calculatenumbers import Calc
                      query = query.replace("calculate","")
                      query = query.replace("saphi","")
                      Calc(query)


 
#location
                elif "where i am" in query or "location" in query or "where we are" in query:
                    speak("Let me check")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                       # print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        country = geo_data['country']
                        speak(f"I think we are in {city} city of {country} country")
                        print(f"I think we are in {city} city of {country} country")
                    except Exception as e:
                        speak("Sorry, due to network issue I am not able to find where we are")    
                        pass


#to check insatgram profile
                elif "instagram profile" in query or "profile on instagram" in query:
                    speak("Please enter the user name correctly")
                    name = input("Enter username here: ")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"here is the profile of the user{name}")
                    time.sleep(5)
                    speak("Would you like to download profile picture of this account")
                    condition = takeCommand().lower()
                    if "yes" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name, profile_pic_only = True)
                        speak("profile picture is saved in your main folder")
                    else:
                        pass    

#weather or temperature
                elif "temperature" in query:
                    search = "temperature in Kharar" 
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)  
                    data = BeautifulSoup(r.text,"html.parser") #it will give the text
                    temp = data.find("div", class_ = "BNeawe").text 
                    speak(f"current{search} is {temp}") 
                    

                elif "weather" in query:
                    search = "temperature in Kharar" 
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)  
                    data = BeautifulSoup(r.text,"html.parser") #it will give the text
                    temp = data.find("div", class_ = "BNeawe").text 
                    speak(f"current{search} is {temp}") 


#alarm
                elif "set an alarm" in query.lower():
                    speak("Please tell the time, for example: 5:30 AM")
                    tt = input("Enter the time for alarm (e.g., '5:30 AM'): ").strip()  # This should capture the voice input for time
                    tt = tt.replace("set alarm to", "")
                    tt = tt.replace(".", "")
                    tt = tt.upper()
                    import MyAlarm
                    MyAlarm.alarm(tt)
                    
                    

#exact time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strTime}")   

                elif "finally sleep" in query:
                    speak("Going to sleep")
                    exit()  


#remeber function
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("saphi", "") 
                    speak("You told me "+ rememberMessage)
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    remembered_message = remember.read()
                    speak("You told me " + remembered_message)
                    print("You told me " + remembered_message)
                    remember.close()        


    #shutdown
                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdown?")
                    speak("Please say yes or no.")
                    shutdown = takeCommand().lower()
                    if "yes" in shutdown:
                        os.system("shutdown /s /t 1")
                    elif "no" in shutdown:
                        speak("Shutdown aborted.") 








       






