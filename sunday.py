
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
##print(voices)
engine.setProperty('voice',voices[0].id)
def speak(voice):
    engine.say(voice)
    engine.runAndWait()
def wishMe():
    hr=datetime.datetime.now().hour
    if(hr>=2 and hr<12):
        speak("Good Morning, Have a nice day Utkarsh")
    elif(hr>=12 and hr<16):
        speak("Good afternoon Utkarsh")
    elif(hr>=16 and hr<22):
        speak("Goopd Evening Utkarsh, Hope you are having a good day")
    else:
        speak("Good Night Utkarsh, have a good sleep")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes Utkarsh??\nListening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognising.....")
        query=r.recognize_google(audio,language='en-in')
        print("User said ",{query})
        #speak(query)
    except Exception as e:
        print("Sorry Utkarsh can't here you\nPlease speak again")
        return "none"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('duttutkarsh2911@gmail.com', 'PPPP')
    server.sendmail('duttutkarsh2911@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            query=query.replace("wikipedia","")
            print("Searching Wikipedia...")
            result=wikipedia.summary(query,sentences=1)
            speak("According to Wikkipedia")
            print(result)
            speak(result)
            print("\n")
        elif 'sleep sunday' in query:
            print("Sleeping")
            speak("Sleeping, Good night Utkarsh. Untill we meet again")
            #speak(" Untill we meet again")
            break
        elif 'open youtube' in query:
            #webbrowser.open("youtube.com")
            webbrowser.get().open('http://www.youtube.com')
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open gmail' in query:
            #webbrowser.open("gmail.com")
            webbrowser.get().open('http://www.gmail.com')
        elif 'open google' in query:
            #.open("google.com")
            #webbrowser.get('windows-default').open('http://www.google.com')
            #webbrowser.get().open('http://www.google.com')
            webbrowser.open("https://www.google.com")
        elif 'play music' in query:
            dirr='D:\\Songs'
            songs=os.listdir(dirr)
            print(dirr)
            os.startfile(os.path.join(dirr,songs[5]))
        elif 'the time' in query:
            tt=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir Time is {tt}\n")
            print("Sir,Time is ",tt)
        elif 'open code' in query:
            pat = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(pat)
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ud2911@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
        else:
            continue
#C:\Users\user\AppData\Local\Programs\Python\Python39