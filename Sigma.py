from http import server
import smtplib
import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import wikipedia 
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am SIGMA. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("","")
    server.sendmail("",to,content)
    server.close








wishMe()
while True:
    query = takeCommand().lower()
    if "wikipedia" in query:
        speak("Searching wikipedia...")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("According to  wikipedia...")
        speak(results)

    elif "open website" in query:
        speak("what website should i open sir")
        s=takeCommand()
        webbrowser.open(f"{s}.com")
    elif "play music" in query:
        music_dir="C:\\Users\\lalit\\OneDrive\\Desktop\\songs"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))  
    elif "time" in query:
        str=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {str}")
    elif "open code" in query:
        path="C:\\Users\\lalit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
    elif "send email" in query:
        try:
            speak("what should i say?")
            content=takeCommand()
            to=""
            sendEmail(to,content)
            speak("email has been sent")
        except Exception as e:
            speak("Sorry lalith i am not able to send the mail")
    elif "exit" in query:
        break
    

