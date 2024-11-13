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
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from saphiUi import Ui_saphi
import sys




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id) #selecting voice
# print(voices[0])
engine.setProperty("rate",200) #rate at which it will speak



class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()    
    
    def speak(self, audio): #how will it speak
        engine.say(audio)
        engine.runAndWait() #wait after speaking


    def takeCommand(self):
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
        

    
#alarm

    def alarm(self, query):
        timehere = open("Alarmtext.txt", "a")
        timehere.write(query)
        timehere.close()
        os.startfile("alarm.py")

#pdf reader


   


    
    def TaskExecution(self):
        while True:
             self.query = self.takeCommand() or ""  # Defaults to empty string if None

        # Ensure self.query is a valid string before using it
             self.query = self.query.lower()
            
            # Greet function
             if "wake up" in self.query:
                from greet import greetMe
                greetMe()

                while True:
                    self.query = self.takeCommand()
                    
                    self.query = self.query.lower()
                        
                    if "go to sleep" in self.query:
                        self.speak("Slipping into stealth mode... I'll be quietly recharging. Call me when it's time for the next adventure!")
                        break
                    

    #scheduling the day
                    elif "schedule my day" in self.query:
                        tasks = [] #Empty list 
                        self.speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        self.query = self.takeCommand().lower()
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
                    elif "no" in self.query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()  


    #show schedule
                    elif "show my schedule" in self.query:
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
    #focus mode1
                    elif "focus mode" in self.query:
                        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                        if (a==1):
                            self.speak("Entering the focus mode....")
                            os.startfile("C:\\Users\\Pragya Pakhi\\Desktop\\saphi\\FocusMode.py")
                            exit()

                        
                        else:
                            pass                             
    #open any app
                    elif "open" in self.query:   #EASY METHOD
                        self.query = self.query.replace("open","")
                        self.query = self.query.replace("saphi","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")                     

    #internet speed
                    elif "internet speed" in self.query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576         
                        download_net = wifi.download()/1048576
                        print(f"Wifi Upload Speed is {upload_net:.2f} Mbps")
                        print(f"Wifi Download Speed is {download_net:.2f} Mbps")
                        self.speak(f"Wifi download speed is {download_net:.2f} Mbps")
                        self.speak(f"Wifi upload speed is {upload_net:.2f} Mbps")

    #screenshot function         
                    elif "screenshot" in self.query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save(r"C:\\Users\\Pragya Pakhi\\Pictures\Screenshots\ss.jpg") 

    #camera
                    elif "click my photo" in self.query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        self.speak("SMILE")
                        pyautogui.press("enter")    

    #read pdf
                    

    #hide files and folder
                    elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                        self.speak("Do you want to hide this folder or make it visible for everyone")
                        condition = self.takeCommand().lower()
                        if "hide" in condition:
                            self.speak("Please provide the full path of the file or folder you want to hide.")
                            file_path = input("Please enter the full path of the file or folder you want to hide: ")
    # Capture the file path input from the user
                            os.system(f'attrib +h "{file_path}"')
                            self.speak(f"The file or folder is now hidden.")
                            self.speak("All the files are now hidden.")
                        elif "visible" in condition:
                            self.speak("Making all hidden files visible.")
                            os.system("attrib -h /s /d")  # Unhide all files and folders
                            self.speak("All hidden files are now visible to everyone.")
                        elif "leave it" in condition or "leave for now" in condition:
                            self.speak("Ok")            
            
    #greetings 
                    elif "hello" in self.query:
                        self.speak("Hello, How are you? I am Saphi Let’s dive in—what's on your mind?")
                    elif "i am fine" in self.query:
                        self.speak("that's great")
                    elif "how are you" in self.query:
                        self.speak("I am perfect")
                    elif "thank you" in self.query:
                        self.speak("You're welcome") 
    #playlist
                    elif "tired" in self.query:
                        self.speak("Playing your favourite songs")
                        a = (1,2,3)
                        b = random.choice(a)
                        if b==1:
                            webbrowser.open("https://www.youtube.com/watch?v=PqFMFVcCZgI")
                        elif b == 2:
                            webbrowser.open("https://www.youtube.com/watch?v=tgVYh94QH8k")  
                        elif b==3:
                            webbrowser.open("https://www.youtube.com/watch?v=mH_LFkWxpI0")     

    #jokes
                    elif "tell me a joke" in self.query:
                        joke = pyjokes.get_joke()
                        print(joke)
                        self.speak(joke)

    #switch window
                    elif "switch the window" in self.query:
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.keyUp("alt")  

    #email to --
                    
                    elif "email to sumit" in self.query:
                        self.speak("Do You want to send a file: ")
                        query = self.takeCommand().lower()
                        
                        if "yes" in self.query:
                            email= 'pragya93045@gmail.com'
                            password = 'xutr tfer qrco ihpg'
                            send_to_email = 'sklegacy789@gmail.com'
                            self.speak("What is the subject for this email")
                            query = self.takeCommand().lower()
                            subject = query
                            self.speak("What is the message for this email")
                            query2 = self.takeCommand().lower()
                            message = query2
                            self.speak("Please enter the correct path of the file into the shell")
                            file_location = input("Please enter the path here: ")

                            self.speak("Please wait, I am sending email now")

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
                            self.speak("Email has been sent")
                    
                        if "no" in self.query:
                            email= 'pragya93045@gmail.com'
                            password = 'xutr tfer qrco ihpg'
                            send_to_email = 'sklegacy789@gmail.com'
                            self.speak("What is the subject for this email")
                            self.query = self.takeCommand().lower()
                            subject = query
                            self.speak("What is the message for this email")
                            self.query2 = self.takeCommand().lower()
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
                            self.speak("Email has been sent")






                        

    #youtube controls
                    elif "pause" in self.query:
                        pyautogui.press("k")
                        self.speak("video paused")
                    elif "play" in self.query:
                        pyautogui.press("k")
                        self.speak("video played")
                    elif "mute" in self.query:
                        pyautogui.press("m")
                        self.speak("video muted") 

                    elif "unmute" in self.query:
                        pyautogui.press("m")
                        self.speak("video unmuted")     

                    elif "volume up" in self.query:
                        from keyboard import volumeup
                        self.speak("Turning volume up")
                        volumeup()

                    elif "volume down" in self.query:
                        from keyboard import volumedown
                        self.speak("Turning volume down")
                        volumedown()              


    #to open apps


                    elif "open" in self.query:
                        from Dictapp import openappweb
                        openappweb(self.query)
                    elif "close" in self.query:
                        from Dictapp import closeappweb
                        closeappweb(self.query)    









                    elif "google" in self.query:
                        from searchNow import searchGoogle
                        searchGoogle(self.query)
                    elif "youtube" in self.query:
                        from searchNow import searchYoutube
                        searchYoutube(self.query)
                    elif "wikipedia" in self.query:
                        from searchNow import searchWikipedia 
                        searchWikipedia(self.query)

    #news function
                    elif "news" in self.query:
                        from NewsRead import latestnews
                        latestnews()      
    #calculator
                    elif"calculate" in self.query:
                        from Calculatenumbers import WolfRamAlpha
                        from Calculatenumbers import Calc
                        self.query = self.query.replace("calculate","")
                        self.query = self.query.replace("saphi","")
                        Calc(self.query)

    #whatsapp
                    elif "whatsapp" in self.query:
                        from Whatsapp import sendMessage
                        sendMessage()
    
    #location
                    elif "where i am" in self.query or "location" in self.query or "where we are" in self.query:
                        self.speak("Let me check")
                        try:
                            ipAdd = requests.get('https://api.ipify.org').text
                        # print(ipAdd)
                            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                            geo_requests = requests.get(url)
                            geo_data = geo_requests.json()
                            city = geo_data['city']
                            country = geo_data['country']
                            self.speak(f"I think we are in {city} city of {country} country")
                            print(f"I think we are in {city} city of {country} country")
                        except Exception as e:
                            self.speak("Sorry, due to network issue I am not able to find where we are")    
                            pass


    #to check insatgram profile
                    elif "instagram profile" in self.query or "profile on instagram" in self.query:
                        self.speak("Please enter the user name correctly")
                        name = input("Enter username here: ")
                        webbrowser.open(f"www.instagram.com/{name}")
                        self.speak(f"here is the profile of the user{name}")
                        time.sleep(5)
                        self.speak("Would you like to download profile picture of this account")
                        condition = self.takeCommand().lower()
                        if "yes" in condition:
                            mod = instaloader.Instaloader()
                            mod.download_profile(name, profile_pic_only = True)
                            self.speak("profile picture is saved in your main folder")
                        else:
                            pass    

    #weather or temperature
                    elif "temperature" in self.query:
                        search = "temperature in Kharar" 
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)  
                        data = BeautifulSoup(r.text,"html.parser") #it will give the text
                        temp = data.find("div", class_ = "BNeawe").text 
                        self.speak(f"current{search} is {temp}") 
                        

                    elif "weather" in self.query:
                        search = "temperature in Kharar" 
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)  
                        data = BeautifulSoup(r.text,"html.parser") #it will give the text
                        temp = data.find("div", class_ = "BNeawe").text 
                        self.speak(f"current{search} is {temp}") 


    #alarm
                    elif "set an alarm" in self.query:
                        print("input time example: 10 and 10 and 10")
                        self.speak("Set the time")
                        a = input("Please tell the time :-")
                        self.alarm(a)
                        self.speak("Done")


                    elif "the time" in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        self.speak(f"The time is {strTime}")   

                    elif "finally sleep" in self.query:
                        self.speak("Going to sleep")
                        exit()  


    #remeber function
                    elif "remember that" in self.query:
                        rememberMessage = self.query.replace("remember that", "")
                        rememberMessage = self.query.replace("saphi", "") 
                        self.speak("You told me "+ rememberMessage)
                        remember = open("Remember.txt", "w")
                        remember.write(rememberMessage)
                        remember.close()

                    elif "what do you remember" in self.query:
                        remember = open("Remember.txt", "r")
                        self.speak("You told me "+remember.read())    


        #shutdown
                    elif "shutdown the system" in self.query:
                        self.speak("Are you sure you want to shutdown?")
                        self.speak("Please say yes or no.")
                        shutdown = self.takeCommand().lower()
                        if "yes" in shutdown:
                            os.system("shutdown /s /t 1")
                        elif "no" in shutdown:
                            self.speak("Shutdown aborted.") 

startExecution = MainThread()

    #if __name__ == "__main__":
      #  TaskExecution()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_saphi()
        self.ui.setupUi(self)
        #self.ui = self.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/7kmF.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/T8bahf (1).gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)




       


app = QApplication(sys.argv)
saphi = Main()
saphi.show()
exit(app.exec_())




