import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id) #selecting voice
# print(voices[0])
engine.setProperty("rate",200) #rate at which it will speak

def speak(audio): #how will it speak
    engine.say(audio)
    engine.runAndWait() #wait after speaking


def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
               "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
               "sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
               "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
               "politics" : "https://newsapi.org/v2/everything?q=tesla&from=2024-09-03&sortBy=publishedAt&apiKey=4a04ed92709c45b89d65eb6ad2b89772"}

    content = None
    url = None

    speak("Which field news do you want, [business], [entertainment], [health], [science], [sports], [technology], [politics]")
    field = input("Type field news that you want: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news: ")  

    arts = news["articles"]
    for articles in arts:       
            article = articles["title"]
            print(article)
            speak(article)
            news_url = articles["url"]
            print(f"for more info visit: {news_url}")

            a = input("[press 1 to cont] and [press 2 to stop]")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

    speak("thats all")        

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
        "health": "https://newsapi.org/v2/top-headlines?category=health&apiKey=4a04ed92709c45b89d65eb6ad2b89772",  # No country for health
        "science": "https://newsapi.org/v2/top-headlines?category=science&apiKey=4a04ed92709c45b89d65eb6ad2b89772",  # No country for science
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4a04ed92709c45b89d65eb6ad2b89772",
        "politics": "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=4a04ed92709c45b89d65eb6ad2b89772"
    }

    speak("Which field news do you want, [business], [entertainment], [health], [science], [sports], [technology], [politics]")
    field = input("Type field news that you want: ")
    url = None

    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(f"URL Found: {url}")
            break

    if not url:  
        print("URL not found")
        return  

    response = requests.get(url)
    news = response.text
    print(f"API Response: {news}")
    news = json.loads(news)

    if "articles" not in news or not news["articles"]:
        print("No articles found in the response")
        speak("Sorry, no news available right now.")
        return

    speak("Here is the first news:")

    arts = news["articles"]
    for articles in arts:
        print(f"Article Title: {articles['title']}")
        article = articles["title"]
        if article:  
            speak(article)
        else:
            speak("No title available for this article.")

        news_url = articles["url"]
        print(f"For more info visit: {news_url}")

        a = input("[press 1 to continue] and [press 2 to stop]: ")
        if a == "1":
            continue
        elif a == "2":
            break

    speak("That's all")
