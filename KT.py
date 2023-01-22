import speech_recognition as jv
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
from bs4 import BeautifulSoup
import requests
import random
import pyscreenshot
import aiml
import yt_playlist_downloader

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[5].id)
newVoiceRate = 185
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    #take string and output the voice(read the string)
    engine.say(audio)
    engine.runAndWait()

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = response.get("city")
    return city
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def screenshot():
    image = pyscreenshot.grab()
    image.show()
    num = random.randint(0,1000)
    #image.save('ss' + str(num) + '.png')

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    temp = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(temp+"°C")
    return (location, time, info, temp)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning  thshaan,")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  thshaan,")
    else:
        speak("Good Evening  thshaan,")
    speak ("How can i help you,")

def takeCommand():
    #take input from microphone and return string output
    r = jv.Recognizer()
    with jv.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print(" Thushaan, Can you repeat that one again.")
        return "None"
    return query

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles='std-startup.aiml', commands = 'load aiml b')

if __name__ == "__main__":
    wishMe()
    x = 0
    max_songs = 0
    while True:
        query = takeCommand().lower()
        response = kernel.respond(query) 
        if 'Cj' in query or 'cj' in query:
            speak('yes thshaan?')

        elif 'open youtube' in query or 'goto youtube' in query:
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
        
        elif 'are you there' in query:
                speak('i am here thshaan.')

        elif 'thank you' in query:
                speak('happy to help thshaan')

        elif 'weather' in query and 'today' in query:
                my_city = str(get_location())
                my_city =  my_city + 'weather'
                location , time, info, temp = weather(my_city)
                speak ('In ' + location) 
                speak ('At : ' + time)
                speak ('Its  ' + info + ' outside')
                speak ('And the temperatur is ' + temp + ' celcius')

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

        elif "life" in query and "reminder" in query:
            life = open("life_advice.txt","r")
            content = life.read()
            print(content)
            speak(content)

        elif response != 'Hmm.':
            speak(response)
            print("Jv > "+response)

        else:
            continue

