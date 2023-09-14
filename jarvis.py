import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Voices options
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# Listen to the mic and return the text
def transform():
    r = sr.Recognizer()

    # Setting mic
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print('...')

        # Save audio
        audio = r.listen(origen)

        # noinspection PyBroadException
        try:
            quest = r.recognize_google(audio, language="es-col")
            print(quest)
            return quest
        except sr.UnknownValueError:
            print("No te entiendo")
            return "Sigo esperando"
        except sr.RequestError:
            print("No te entiendo")
            return "sigo esperando"
        except:
            print("Algo ha salido mal")
            return "sigo esperando"


def talk(message):
    # Turn on pyttsx3 and say message
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    engine.say(message)
    engine.runAndWait()


def say_day():
    day = datetime.datetime.today()
    print(day)
    week_day = day.weekday()
    print(week_day)
    week = {0: 'Lunes',
            1: 'Martes',
            2: 'Miércoles',
            3: 'Jueves',
            4: 'Viernes',
            5: 'Sábado',
            6: 'Domingo'}
    talk(f'Hoy es {week[week_day]}')


def say_hour():
    hour = datetime.datetime.now()
    hour = f'En este momento son las {hour.hour} horas con {hour.minute} minutos'
    talk(hour)


def greeting():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = 'Buenas Noches'
    elif 6 <= hour.hour < 13:
        moment = 'Buenos dias'
    else:
        moment = 'Buenas tardes'

    talk(f'{moment} señor Heiderr, en que le puedo ayudar?')


# Central function
def yemora():
    greeting()
    start = True
    while start:
        request = transform().lower()
        if 'abre youtube' in request:
            talk('Estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abre el navegador' in request:
            talk('Estoy abriendo el navegador de google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'pon travis' in request:
            talk('Reproduciendo al travieso')
            webbrowser.open('https://www.youtube.com/watch?v=xl5LunV-OkU&ab_channel=TravisScottVEVO')
            continue
        elif 'qué día es hoy' in request:
            say_day()
            continue
        elif 'qué hora es' in request:
            say_hour()
            continue
        elif 'busca en wikipedia' in request:
            request = request.replace('busca en wikipedia', '')
            request = request.replace('de mora', '')
            request = request.replace('ahora', '')
            wikipedia.set_lang('es')
            re = wikipedia.summary(request, sentences=1)
            talk('Segun wikipedia: ')
            talk(re)
            continue
        elif 'busca en internet' in request:
            request = request.replace('busca en internet', '')
            request = request.replace('de mora', '')
            request = request.replace('ahora', '')
            pywhatkit.search(request)
            talk('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in request:
            pywhatkit.playonyt(request)
            continue
        elif 'broma' in request:
            talk(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in request:
            acc = request.split('de')[-1].strip()
            cart = {'apple': 'AAPPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                search = cart[acc]
                search = yf.Ticker(search)
                price = search.info['regularMarketPrice']
                talk(f'El precio de {acc} es {price}')
                continue
            except:
                talk('Perdon, no la he encontrado')
        elif 'adios' in request:
            talk('Si me necesites estare aqui')


yemora()
