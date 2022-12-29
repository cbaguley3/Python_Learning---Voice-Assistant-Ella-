import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import sys
sys.path.append('/usr/local/lib/python3.7/dist-packages/')
import pyjokes
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)

# Zira voice id
voice_id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#hear in the mic and return the audio as text
def transform_audio_into_text():

    # store recognizer in variable
    r = sr.Recognizer()

    # mic settings 
    r.energy_threshold = 200

    # set microphone
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can now speak")

        # save what you hear as audio
        audio = r.listen(source)

        try:
            # search on Google
            request = r.recognize_google(audio, language="en-us")

            # test in text
            print("You said " + request)

            #return request
            return request

        # if audio is not understood
        except sr.UnknownValueError:

            # show proof that it didn't understand the audio
            print("Oops! I didn't understand audio")

            # return error
            return "I am still waiting"

        # In case the request can't be resolved
        except sr.RequestError:
            
            # show proof that it didn't understand the audio
            print("Oops! I can't find service")

            # return error
            return "I am still waiting"

        # Unexpected error
        except:
            # show proof that it didn't understand the audio
            print("Oops! Something went wrong. I will try to find out more")

            # return error
            return "I am still waiting"

# function so the assistant can be heard
def speak(message):

    # start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id1)

    # deliver message
    engine.say(message)
    engine.runAndWait()

#Inform day of the week
def ask_day():

    # Create a variable with today's information
    day = datetime.date.today()
    print(day)

    # Variable for day of the week
    week_day = day.weekday()
    print(week_day)

    # Names of days
    calender = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # Say the day of the week
    speak(f'Today is {calender[week_day]}')

# Inform what time it is
def ask_time():

    # variable with time information
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours and {time.minute} minutes'
    print(time)

    # say the time
    speak(time)

# Initial greeting
def initial_greeting():

    # greeting message
    speak('Hello, my name is Ella. How can I help you?')

# Main function of the assistant
def my_assistant():
    #Activate the initital greeting
    initial_greeting()
    
    #cut-off variable
    go_on = True

    # Main loop
    while go_on:
        # Activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('No problem, I am opening youtube for you now')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            speak ('Of course, I am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue
        elif 'what time is it?' in my_request:
            ask_time()
            continue
        elif 'do a wikipedia search for' in my_request:
            speak('Please, give me a second. I am looking for it now.')
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences=1)
            speak('Found it. According to wikipedia: ')
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak('of course, looking now')
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('here is everything that I found')
            continue
        elif 'play' in my_request:
            speak('oh, I think that sounds like a good idea. I will play it now') 
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak(pyjokes.get.joke(language='en', category='neutral'))
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL',
                         'bitcoin': 'BTC',
                         'ethereum': 'ETH'}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it! The price of {share} is {price}')
                continue
            except:
                speak('I am sorry, but I could not find that information')
                continue
        elif 'thank you' in my_request:
            speak('I am glad I could help. Let me know if there is anything else I can do')
            break



my_assistant()