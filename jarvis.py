import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<15:
        speak("Good Afternoon!")   

    elif hour>=15 and hour<19:
        speak("Good Evening!") 

    else:
        speak("Good Night!")  

    speak("Hi Goarav, I am your assistant. Please tell me how may I help you")       

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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

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
            webbrowser.open("youtube.com")
        
        elif 'flat class' in query:
            webbrowser.open("https://teams.microsoft.com/_#/school/conversations/FORMAL%20LANGUAGE%20and%20AUTOMATA%20THEORY%20(PCC-CS502)?threadId=19:5739ca4cfc2a44689758b97ef3188f31@thread.tacv2&ctx=channel")

        elif 'cs class' in query:
            webbrowser.open("https://teams.microsoft.com/_#/school/conversations/COMPUTATIONAL%20STATISTICS?threadId=19:951fedfd2cc44e7086388f8bd5529794@thread.tacv2&ctx=channel")
        
        elif 'object programming class' in query:
            webbrowser.open("https://teams.microsoft.com/_#/school/conversations/Object%20Oriented%20Programming(PCC-CS503)?threadId=19:fcb2955bcb7a4d3d9823aae418219908@thread.tacv2&ctx=channel")

        elif 'software engineering class' in query:
            webbrowser.open("https://teams.microsoft.com/_#/school/conversations/SOFTWARE%20ENGINEERING?threadId=19:a5de608f59ec47acb949164084611c84@thread.tacv2&ctx=channel")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'where is' in query or 'where\'s' in query:
            query = query.replace("where is", "")
            webbrowser.open(f'https://www.google.nl/maps/place/?q={query}')
            speak("here is where it is.")

        elif 'when is' in query or 'when\'s' in query:
            query = query.replace("when is", "")
            webbrowser.open(f'https://www.google.com/search?q=when+is+{query}&rlz=1C1CHBF_enIN856IN856&oq=when+is+&aqs=chrome.1.69i59l2j0i67j0i131i433j0j0i433j0l2.4035j0j7&sourceid=chrome&ie=UTF-8')
            speak(f"{query} is on.")

        elif 'on youtube' in query:
            query = query.replace("on youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            speak(f" showing {query} on youtube.")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Gaurav7.G7\\Desktop\\SONGS-MP3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Users\\Gaurav7.G7\\Desktop\\Google Chrome.lnk"
            os.startfile(codePath)

        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kumargaurav20122000@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    





#temprature
# google search
# open microsoft word, ppt
# stop listening
# bluetooth pairing
# nearby places
# search in amazon/check price of something
# add in to do list
# reminder
# setting alarm
# calendar-ask google about the date
# tell me the news
# covid cases in delhi, in india, today, each week
# open teams, specific classes
# open speech recognition in notepat
# read books