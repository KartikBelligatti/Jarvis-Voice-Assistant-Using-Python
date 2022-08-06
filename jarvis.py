import cap as cap
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis sir, please tell me what can i do for you")

if __name__ == "__main__":
    wish()
    # while True:
    if 1:
        query = takecommand().lower()

        #logic
        if "open notepad" in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open adobe reader' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\AcroRd32.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir="C:\\Users\\ASUS\\Music\\Hindi"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")


        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")
        elif "open linkedin" in query:
            speak("opening linked in")
            webbrowser.open("www.linkedin.com")
        elif "open github" in query:
            speak("opening github")
            webbrowser.open("www.github.com")
        elif "open WhatsApp" in query:
            speak("opening whatsapp")
            webbrowser.open("www.whatsapp.com")
