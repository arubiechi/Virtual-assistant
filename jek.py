import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import math
#import smtplib


print("Mengaktifkan Jek")
MASTER = "Master"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
   
    

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <12:
        speak("Selamat Pagi" + MASTER)

    elif hour>=12 and hour<18:
        speak("Selamat Siang" + MASTER)

    else:
        speak("Selamat Malam" + MASTER)

    speak("Jek siap menerima perintah. Ada yang bisa dibantu?")


#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan...")
        audio = r.listen(source)

    try :
        print("Mencari...")
        query = r.recognize_google(audio, language = 'id')
        print(f"Master bilang: {query}\n")

    except Exception as e:
       print("coba ulang...")
       query = ''
    

    return query

#main program starting
def main():
    speak("Mengaktifkan Jek")
    wishMe()
    while True:
        query = takeCommand()

        #Logic for executing tasks as per the query
        if query == 'keluarkan program':
            speak('Terimakasih. selamat beristirahat.')
            break
        else:
            if query==None:
                pass
            elif 'wiki' in query.lower():
                
                query = query.replace ("Wiki", " ")
                speak(f'mencari...{query} dalam wikipedia' )
                wikipedia.set_lang('id')
                results = wikipedia.summary(query, sentences =2)
                print(results)
                speak(f'menurut wikipedia. {results}')
                            
            #elif 'cari' in query.lower():
                #query = query.replace("cari", "")
                #speak(f'mencari...{query}' )
                
            # results = googlesearch.search(query,num_results=2)
                #print(results)
                #speak(results)

            elif 'buka youtube' in query.lower():
                #webbrowser.open('youtube.com')
                query = query.lower().replace("buka youtube", "")
                speak(f'membuka youtube {query}')
                
                url = f"https://www.youtube.com/results?search_query={query}"
                brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
                webbrowser.get(brave_path).open(url)

            elif 'googling' in query.lower():
                #webbrowser.open('youtube.com')
                query=query.replace("Googling", "")
                speak(f'membuka google {query}')
                url = f"https://www.google.com/search?q={query}"
                chrome_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
                webbrowser.get(chrome_path).open(url)

            elif 'mainkan musik' in query.lower():
                speak('Oke bang....')
                songs_dir = "D:\\mp3"
                songs = os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir, songs[0]))
            elif 'matikan komputer' in query.lower():
                speak('Mematikan komputer')
                      
                
                os.system('shutdown /s /t 30')


            elif 'hitung keliling lingkaran' in query.lower():
                speak('Sebutkan diameter lingkaran')
                diameter=takeCommand()
                keliling=math.pi*int(diameter)
                print(keliling)
                speak(f'keliling lingkaran adalah {keliling} satuan')

            elif 'jam berapa sekarang' in query.lower():
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f" Sekarang jam {strTime}")

            elif 'buka aplikasi kode' in query.lower():
                codePath = "C:\\Users\\Rahmat Budi Haryono\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            

main()