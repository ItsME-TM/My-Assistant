import speech_recognition as Tmax
import pyttsx3
import datetime
import wikipedia
import time
import webbrowser
import os
import pywhatkit
import random
import pyscreenshot
import aiml
import yt_playlist_downloader

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = Tmax.Recognizer()
    with Tmax.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Thshan: {query}\n")
    except Exception as e:
        print(e)
        print(" Thushaan, Can you repeat that one again.")
        return "None"
    return query

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def screenshot():
    image = pyscreenshot.grab()
    image.show()
    num = random.randint(0,1000)


def wishMe():
    time.sleep(0.5)
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning  thshaan,")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  thshaan,")
    else:
        speak("Good Evening  thshaan,")
    speak ("How can i help you,")

kernel = aiml.Kernel()
kernel.bootstrap(brainFile="D:/Programmes/Python/My_project_1_Tmax/brain.brn")
if __name__ == "__main__":
    wishMe()
    x = 0
    max_songs = 0
    while True:
        query = takeCommand().lower()
        response = kernel.respond(query) 
        if 'open youtube' in query or 'goto youtube' in query:
                speak ('okay  thshaan. Opening you tube.')
                webbrowser.open("youtube.com")

        elif 'open google' in query or 'goto google' in query:
            speak('okay  thshaan. Opening google.')
            webbrowser.open('google.com')

        elif 'search' in query and 'in google' in query:
            query = query.replace('search', '')
            query = query.replace('in google', '')
            pywhatkit.search(query)

        elif 'download' in query and 'youtube playlist' in query:
            speak('ofcourse i can, give me the youtube playlist link.')
            yt_playlist_downloader.yt_playlist()
            speak('thshaan, your playlist is ready to be played.')
        
        elif 'wikipedia' in query:
            speak('Searching in Wikipedia.')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 4)
            speak("According to Wikipedia,")
            print(results)
            speak(results)
        
        elif 'play' in query and 'youtube' in query:
            query = query.replace('play', '')
            query = query.replace('in youtube', '')
            speak('okay  thshaan, playing ' + query)
            pywhatkit.playonyt(query)

        elif 'play some music' in query or 'play music' in query:
            speak('Finding songs. Found two playlists. Which playlist you want to play. playlist number one or playlist number two.')
            choice = takeCommand().lower()
            if 'number 1' in choice or '1'in choice:
                music_dir = 'F:\play_list_1'
                songs = os.listdir(music_dir)
                print(songs)
                max_songs = len(songs)
                speak('Starting your song thshaan.')
                x = random.randint(0,max_songs-1)
                os.startfile(os.path.join(music_dir, songs[x]))
            elif 'number 2' in choice or '2' in choice:
                music_dir = 'F:\play_list_2'
                songs = os.listdir(music_dir)
                print(songs)
                max_songs = len(songs)
                speak('Starting your song thshaan.')
                x = random.randint(0,max_songs-1)
                os.startfile(os.path.join(music_dir, songs[x]))
            else:
                print(choice)
                speak('Sorry thshaan, i didnt hear it')

        elif 'goto next song' in query or 'next song' in query:
            speak('Playing next song thshaan.')
            x = random.randint(0,max_songs-1)
            os.startfile(os.path.join(music_dir, songs[x]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" thshaan its {strTime}")

        elif 'open' in query and 'microsoft teams' in query:
            microsoft_teams_path = "C:\\Users\\Thushan\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams.exe"
            speak("Opening Microsoft Team  thshaan")
            os.startfile(microsoft_teams_path)

        elif 'open' in query and 'snipping tool' in query:
            speak('opening the snippingtool thshaan')
            os.system('Snippingtool.exe')

        elif "all for now" in query or 'bye' in query:
            speak("Its all ways a pleasure thshaan")
            break

        elif "take" in query and "screenshot" in query:
            speak("Capturing the screen thshaan.")
            screenshot()

        elif "life" in query and "quotes" in query:
            life = open("D:/Programmes/Python/My_project_1_Tmax/life_quotes.txt","r")
            content = life.read()
            print(content)
            speak(content)

        elif response != 'Hmm.':
            time.sleep(0.5)
            speak(response)
            print("Tmax > "+response)

        else:
            continue

