import speech_recognition as sr
import webbrowser
import pyttsx3
import music_Libraries
from openai import OpenAI
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general task    like Alexa and Google Cloud. Give short response please"},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return(completion.choices[0].message)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_Libraries.music[song]
        webbrowser.open(link)
    else:
        #Let openai handle the request
        output = aiProcess(c)
        speak(output)


if __name__== "__main__":
    speak("Initializing Jarvis....")
    while True:
            
        #Listen for the wake word "Jarvis"
        r = sr.Recognizer()
        print("Recognizing")

        # recognize speech using Google
        try:
            #Obtain audio from the microphone 
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))

             