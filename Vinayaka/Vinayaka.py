import pyttsx3  #text-to-speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib  #for sending email
import requests


# To use a voice of a Computer we use sapi5
engine = pyttsx3.init('sapi5') # Speech Application Programming Interface 
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id) # set voice male/female


# use to speak it out from computer
def speak(audio):
    #Converts the given text (audio) to speech.
    engine.say(audio) 
    #Ensures the speech is completed before the code continues.
    engine.runAndWait() 
    
    
# greetings
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hey...Good Morning!")
    elif hour>=12 and hour<18: 
        speak("Hey...Good Afternoon!")
    else:
        speak("Hey...Good Evening!")
        
    speak("I am Vinayakaa, How May I Assist You?")
    
    
#It takes microphone input from the user and returns string output
def takeCommand(): 
    #Initialized a speech recognition object from the speech_recognition library.
    r = sr.Recognizer() 
    #Activates the microphone as the input source.
    with sr.Microphone() as source:
        print("Listening...")
        #Maximum amount of silence (in secs)
        r.pause_threshold = 1
        #Listens to the user's input and stores it as audio data.
        audio = r.listen(source)
        
    try:
        print("Recognizing...")    
        #Google's speech recognition to convert the audio input to text in English-In
        query = r.recognize_google(audio, language = 'en-in') 
        print(f"User Said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    joke_data = response.json()
    if joke_data.get("joke"):
        return joke_data["joke"]
    return "Sorry, I couldn't find a joke at the moment."


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YourEmail','YourPassword')
    server.sendmail('YourEmail',to,content)
    server.close()
     

if __name__ == "__main__":
    wishMe()
    i = 0
    task = 0
    while (i<3 and task == 0):
        query = takeCommand().lower()
        
        if 'today is sunday' in query: 
            speak("That's good...You Know Me!, Now tell me what I can do for you,Sir!")
            while True:
                query = takeCommand().lower()
                # Logic for Executing Tasks based on Query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query, sentences = 2)
                    speak("So, According to Wikipedia")
                    print(results)
                    speak(results)
                    task = 1
                    break
                
                elif 'search on google' in query:
                    speak(' What I can search for you...')
                    query = takeCommand().lower()
                    if query != 'none':
                        audio = f"Searching '{query}' On browser..."
                        print(audio)
                        speak(audio)
                        webbrowser.open(f"https://www.bing.com/search?q={query}")
                        task = 1
                        break 
                
                elif 'tell me a joke' in query:
                    joke = get_joke()
                    print(joke)
                    speak(joke)
                    task = 1
                    break
                    
                elif 'search on youtube' in query:
                    speak(' What I can search for you on youtube')
                    query = takeCommand().lower()
                    if query != 'none':
                        audio = f"Searching '{query}' On Youtube..."
                        print(audio)
                        speak(audio)
                        webbrowser.open(f"https://www.youtube.com/results?sp=mAEB&search_query={query}")
                        task = 1
                        break 
                
                elif 'search on spotify' in query:
                    speak(' What I can search for you on spotify')
                    query = takeCommand().lower()
                    if query != 'none':
                        audio = f"Searching '{query}' On Spotify..."
                        print(audio)
                        speak(audio)
                        webbrowser.open(f"https://open.spotify.com/search/{query}")
                        task = 1
                        break 
                    
                elif 'open youtube' in query:
                    speak("  Sure Sir...I am opening Youtube for you.")
                    webbrowser.open("youtube.com")
                    task = 1
                    break
                
                elif 'shutdown' in query:
                    speak(" Shutting Down the System in 3 seconds")
                    os.system("shutdown /s /t 3")
                    task = 1
                    break
                    
                elif 'open lead code' in query:
                    speak("  Sure Sir...I am opening LeetCode for you.")
                    webbrowser.open("leetcode.com")
                    task = 1
                    break
                    
                elif 'open google' in query:
                    speak("  Sure Sir...I am opening Google for you.")
                    webbrowser.open("google.com")
                    task = 1
                    break
                
                elif 'open chess' in query:
                    webbrowser.open("chess.com")
                    task = 1
                    break
                
                elif 'play online games' in query:
                    webbrowser.open("poki.com")
                    task = 1
                    break
                
                elif 'open time table' in query:
                    webbrowser.open("Update with your time table link")
                    task = 1
                    break
                
                elif 'play music on spotify' in query:
                    webbrowser.open("Update with spotify link or any playlist list")
                    task = 1
                    break
                
                elif 'play music on youtube' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=w402dXxAO3c&list=PLummYxZcETxcVoFlS5q38HZm0Eg2g8D-P&pp=gAQBiAQB8AUB")
                    task = 1
                    break
                    
                elif 'open stackoverflow' in query:
                    speak("  Sure Sir...I am opening stackoverflow for you.")
                    webbrowser.open("stackoverflow.com")
                    task = 1
                    break
                    
                elif 'play music on computer' in query:
                    music_dir = 'Update With Your Directory' # \\ to escape character
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    task = 1
                    break
                    
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f" Sir, the time is {strTime}")
                    
                elif 'open vs code' in query:
                    code_path = "Update with the directory of your VS Code"
                    os.startfile(code_path)
                    task = 1
                    break
                
                elif 'open drive' in query:
                    code_path = "D:\\"
                    os.startfile(code_path)
                    task = 1
                    break
                
                elif 'email to vinayak' in query: # dictionary
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "ReceiverEmail"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        speak("  Sorry Sir , Not able to send this email")
                    task = 1
                    break
                        
                elif 'today is not sunday' in query:
                    speak("  Shitt!!!  You fooled me, Now I'm going to sleep, Take care Sir!")
                    task = 1
                    break
                
                else:
                    speak("  Sorry Sir..., I have some limited features. Try something else")
        else:
            if i == 0:
                speak(" That's a Wrong Password... I don't know Who Are You...two chances left") 
            elif i == 1:
                speak(" Sorry... Again That's a Wrong Password... Be careful, one more chance is left")
            else:
                speak("  Wrong Password... Now I'm Blocking you. GoodBye")
            i += 1
