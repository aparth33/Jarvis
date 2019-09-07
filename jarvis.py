import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from getpass import getpass #getpassword
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server_ssl = smtplib.SMTP('smtp.gmail.com',587)
    server_ssl.ehlo()
    server_ssl.starttls()
    usr=input('Enter Username')
    pwd=getpass("Enter Passsword : ")
    server_ssl.login(usr,pwd)
    server_ssl.sendmail(usr, to, content)
    server_ssl.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.get(chrome_path).open("youtube.com")
        elif 'open github' in query:
            speak("Opening Github")
            webbrowser.get(chrome_path).open("https://github.com/aparth33/Jarvis")
        elif 'open hackerrank' in query:
            speak("Opening Hackerrank")
            webbrowser.get(chrome_path).open("hackerrank.com")
        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.get(chrome_path).open("facebook.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.get(chrome_path).open("stackoverflow.com")  
        elif 'open yahoo' in query:
            speak("Opening Yahoo")
            webbrowser.get(chrome_path).open("yahoo.com") 
        
        
        # elif 'open' in query:
        #     speak('Opening site...')
        #     query=query.replace('open','')
        #     webbrowser.get(chrome_path).open(f"{query}.com")

        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio")
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                to = input('Enter email id to whom you want to send Email : ')    
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")    
        
        
        elif 'open word' in query:
            speak("Opening word")
            wordpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"
            os.startfile(wordpath)
        elif 'open excel' in query:
            speak("Opening excel")
            wordpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk"
            os.startfile(wordpath)
        elif 'open powerpoint' in query:
            speak("Opening powerpoint")
            wordpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk"
            os.startfile(wordpath)
        elif 'who are you' in query:
            speak('I am Jarvis Sir. I was designed by great man, Mister Parth Aggarwal who is a software developer and machine learning enthusiast, He often spends time inn improving me.')
        elif 'when is your birthday' in query:
            speak("I was designed on 8th August 2019")
        elif 'goodbye' in query:
            speak("Good Bye Sir ! Hope you have a great life, It was great working with you ! ")
            speak("shutting down")
            exit()