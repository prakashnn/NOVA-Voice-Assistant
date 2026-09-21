import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary 

recognize = sr.Recognizer()


def speak(text):
    print(text)
    try:
        engine = pyttsx3.init() 
        engine.say(text)
        engine.runAndWait()
        # engine.stop()
    except Exception as e:
        print("Speech engine error:", e)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif"open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif"open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com") 
    elif c.lower().startswith("play"):
        song = c.split(" ") [1]
        # song = c.lower().replace("play", "", 1).strip()
    # Check if the song exists in your music library
        if song in musiclibrary.music:
             link = musiclibrary.music[song]
             webbrowser.open(link)
        else:
           speak(f"Sorry, I don't know the song '{song}'")
if __name__ == "__main__":
    speak("Initializing Nova...")
    while True:
        # r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = recognize.listen(source, timeout=5, phrase_time_limit=5)
            word = recognize.recognize_google(audio)


            if "nova" in word.lower():
                speak("Yes sir")
        
                

                with sr.Microphone() as source:
                  print("Nova is Active...")
                  audio = recognize.listen(source, timeout=5, phrase_time_limit=5)
                  command = recognize.recognize_google(audio)
                  processCommand(command) 
             
              
                 
        except Exception as e:
            print("Error: {0}".format(e))



