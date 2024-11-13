import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300 #the threshold we are speaking and it can listen too. if we put threshold as high we have to shout for it to listen and if low then it will hear the background sound as well
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query    

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #selecting voice
# print(voices[0])
engine.setProperty("rate",170) #rate at which it will speak

def speak(audio): #how will it speak
    engine.say(audio)
    engine.runAndWait()


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap #open google and tell what is in it
       #these are used as we are removing these words to be searched
        query = query.replace("saphi", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on Google")


        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1) #no of lines
            speak(result)

        except:
            speak("NO speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")

        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("saphi", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query) #will open the first video related to the search
        speak("Done")

#it will not open wikipedia but will show the text from wikipedia
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("saphi", "")
        results = wikipedia.summary(query,sentences=2) #it will give summary of the wikipedia and 2 sentences only
        speak("According to wikipedia..")
        print(results)
        speak(results)




    
