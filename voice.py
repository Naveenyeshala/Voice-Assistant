import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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

    speak("I am david. how can i help you today?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:

            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:

            webbrowser.open("https://www.google.com/")
            speak("what should i search in google")
            c=takeCommand().lower()
            webbrowser.open(f"{c}") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is  {strTime}")
            speak(f" the time is {strTime}")

        elif 'open youtube' in query: 
            webbrowser.open("https://www.youtube.com/")
                 
        elif 'open command prompt' in query:
            os.system("start cmd ")

        elif 'no thanks' in query:
            speak("You're welcome! If you have any more questions in the future or need assistance, feel free to reach out. Have a great day!")
            sys.exit()


        speak("do you have any other questions")


    