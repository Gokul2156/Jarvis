import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import random
from client import ask_jarvis


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="2b7651356e864942b6255254bd9dca62"




def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if c.lower()=="open google":
        webbrowser.open("https://google.com")
    elif c.lower()=="open instagram":
        webbrowser.open("https://instagram.com")
    elif c.lower()=="open youtube":
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        songcommand=c.lower().split(" ")#[1]

        if "music"  in songcommand or "song" in songcommand:
            song=random.choice(list(musicLibrary.music.keys()))

            link=musicLibrary.music.get(song)
            speak(f"playing {song}")
            webbrowser.open(link)
        else:
            try:
                song=songcommand[1]
                link=musicLibrary.music.get(song)
                speak(f"playing {song}")
                webbrowser.open(link)
            except IndexError:
                speak("Please specify song name or say play music to play random music")



    

    elif  "news" in c.lower():
        url = "https://newsapi.org/v2/everything?q=India&apiKey=2b7651356e864942b6255254bd9dca62"
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])
        speak("Here are the top headlines")


        for article in articles[:10]:  # Only read top 10
            headlines = article.get("title")
            print(headlines)
            speak(headlines)


    else:
        
        speak("Let me check that for you...")
        print(f"Sending to AI: {c}")
        response = ask_jarvis(c)
        print("Jarvis:", response)
        speak(response)

    
    


if __name__=="__main__":
    speak("Initializing jarvis.....")

    while True:
    #Listen for the wake word "jarvis"
    #obtain audio from microphone

        r=sr.Recognizer()



        print("Recognizing....")
    

        try:
            with sr.Microphone() as source:
                print("Listening")
                audio=r.listen(source,timeout=3,phrase_time_limit=4)
            word=r.recognize_google(audio)
            print(word)

            if word.lower()=="jarvis":
                speak("Hellooo Gokul")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)


                    print(f"Command Recieved {command}")
                    processcommand(command)
                    


        except Exception as e:
            print(f"Error:{e}")


    
