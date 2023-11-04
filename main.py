import win32com.client
import webbrowser
import os
import pyaudio
import speech_recognition

speaker = win32com.client.Dispatch("SAPI.SpVoice")


while 1:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)

def say(text):


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-uk")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error occured. Sorry from jarvis"
        
if __name__ == '__main__':
    print('Niraj')
    say("Hello i am jarvis A.I")

    while True:
        print("Listening...")
        query = takeCommand()
        sites = ["youtube", "https//www.youtube.com"]
        for site in sites:
            if f"open {sites[0]}".lower() in query.lower():
                say(f"openning {site[0]}sir...")
                webbrowser.open(site[1])

        # if open
