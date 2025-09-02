import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
from openai import OpenAI 
import os
 
engine = pyttsx3.init()
r = sr.Recognizer()
keyy="975be7d3df4a478293bbb8b08eca10e2"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def search(text):
    client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key="your api key here",
)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis.",
            },
            {
                "role": "user",
                "content": text,
            }
        ],
        model="openai/gpt-4o",
        temperature=1,
        max_tokens=4096,
        top_p=1
    )

    return response.choices[0].message.content

def command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open my github Account" in c.lower():
        webbrowser.open("https://github.com/Emanijaz15")
    elif "open LinkedIn" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        if song in musiclib.music:
            link = musiclib.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=pk&apiKey={keyy}")
        if r.status_code==200:
            data = r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else:
        output=search(text)
        speak(output)


if __name__ == "__main__":
    speak("Initializing jarvis..")
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio_text = r.listen(source,timeout=5,phrase_time_limit=5)
            text = r.recognize_google(audio_text)
            if text.lower()=="jarvis":
                    speak("Yes ma'am")
                    with sr.Microphone() as source:
                        print("Jarvis active...")
                        audio_text = r.listen(source)
                        text = r.recognize_google(audio_text)
                        command(text)

        except sr.UnknownValueError:
            print("Could not understand audio")



    
