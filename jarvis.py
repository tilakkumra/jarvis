import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("jarvis good morning boss")
        speak("good morining boss")
    elif hour>=12 and hour<17:
        print("good afternoon boss")
        speak("good afternoon boss")
    elif hour>=17 and hour<21:
        print("good evening boss")
        speak("good evening boss")
    else:
        print("good ninght boss")
        speak("good night boss")



def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)

    try:
        print("wait for moments..")
        query=r.recognize_google(audio,language='en-in')
        print(f"you just said: {query}\n")

    except Exception as e:
        print(e)
        speak("please tell me again")
        query="none"
    return query

def wakeupCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is sleeping....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        query="none"
    return query


if __name__=="__main__":
    #wishings()
    while True:
        query=wakeupCommands().lower()
        if "wake up" in query:
            wishings()
            speak("Yes Boss What Can i do for you")
            while True:

                query=commands().lower()
                if "wikipedia" in query:
                    speak("searching in wikipedia")
                    try:
                        query=query.replace("wikipedia","")
                        results=wikipedia.summary(query,sentences=3)
                        speak("According to wikipedia,")
                        print(results)
                        speak(results)
                    except:
                        speak("No Results found sir...")
                        print("No Results found sir...")

                elif "open youtube" in query:
                    speak("opening youtube")
                    pywhatkit.playonyt('arabic kuthu')

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("#H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif "mute" in query:
                    speak("I'm Mutting Sir...")
                    break
                elif 'exit program' in query or 'exit the program' in query:
                    speak("I'm Leaving Sir, Byeee....")
                    quit()

                elif "open google" in query:
                    speak("Opening Google Chrome Sir")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    while True:
                        chromeQuery=commands().lower()
                        if "search" in chromeQuery:
                            youtubeQuery=chromeQuery
                            youtubeQuery=youtubeQuery.replace("search","")
                            pyautogui.write(youtubeQuery)
                            pyautogui.press('enter')
                            speak('searching...')

                        elif "close chrome" in chromeQuery or "exit chrome" in chromeQuery or "leave chrome" in chromeQuery:
                            pyautogui.hotkey('ctrl','w')
                            speak("Closing Google chrome sir...")
                            break

                elif"magic sentence" in query:
                    speak('Yes sir, for your Pleasure!')
                    speak('Viewers please Subscribe to tilak.fun website')
                    speak('And don\'t forget to visit website')
                elif "what can you do for me" in query:
                    speak('Yes sir, nice question')
                    speak('As per my prograam, I am a bot which can perform tasks through you voice contorler')
                elif "cool" in query or "nice" in query or "awsome" in query or "thank you" in query:
                    speak("Yes sir, That's my pleasure!")
                elif "minimize" in query or 'minimise' in query:
                    speak('minimizeing Sir!')
                    pyautogui.hotkey('win','down','down')
                elif "maximize" in query or 'maximise' in query:
                    speak('maximizing Sir!')
                    pyautogui.hotkey('win','up','up')
                elif "close the window" in query or 'close the application' in query:
                    speak('closing Sir')
                    pyautogui.hotkey('ctrl','w')
                elif "screenshot" in query:
                    speak("taking screenshot sir...")
                    pyautogui.press('petsc')
                elif "open paint" in query:
                    speak("opening paint application sir...")
                    os.startfile('C:\\Windows\\System32\\mspaint.exe')
                    while True:
                        paintQuery=commands().lower()
                        if "close" in paintQuery:
                            speak("closing the Application sir")
                            pyautogui.leftClick(x=1344, y=11)
                            break
                        elif "paste" in paintQuery:
                            pyautogui.hotkey('ctrl','v')
                            speak("Done Sir!")
                        elif "save" in paintQuery:
                            pyautogui.hotkey('ctrl','s')
                            speak("saving sir!")
                        elif "minimize" in paintQuery:
                            speak('Minimizing sir')
                            pyautogui.hotkey('win','down','down')
                            break
                        elif "maximize" in paintQuery:
                            speak('maximizeing sir!')
                            pyautogui.hotkey('win','up','up')
                        elif "minimsie" in paintQuery:
                            speak('Minimising sir')
                            pyautogui.hotkey('win','down','down')
                        elif "maximise" in paintQuery:
                            speak('maximiseing sir!')
                            pyautogui.hotkey('win','up','up')
                elif "open notepad" in query:
                    speak("opening notepad Application sir...")
                    os.startfile('C:\\Windows\\System32\\notepad.exe')
                    while True:
                        notepadquery=commands().lower()