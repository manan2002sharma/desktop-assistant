import speech_recognition as sr
import pyttsx3  
import webbrowser



engine = pyttsx3.init()  
r= sr.Recognizer()
text="hello i am atom how can i help you"
def speak(text):
    engine.say(text)
    engine.runAndWait() 

def takecommand():
    k=""
    with sr.Microphone() as source:
        print("kuch bol de..... ")
        audio = r.listen(source)
    try:
        k=r.recognize_google(audio)
        print(k)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return k
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return k
    return k
speak("hello i am atom how can i help you")
""" while True: """
a=takecommand()
if "how are you" in a:
    text="sir i am fine "
    speak(text)
elif "Vishal" in a:
    text="vishal is an idiot"
    speak(text)
elif "Harsh" in a:
    text="Harsh is an idiot and the worst footballer i have ever seen"
    speak(text)
elif "Manan" in a:
    text="Manan Sharma created me and he is most intelligent person i have ever met"
    speak(text)
elif "Chiku" in a:
    text="don't talk  about her , she is ugliest girl i have ever seen"
    speak(text)
elif "Shalini" in a:
    text="she is Manan's mother"
    speak(text)
elif a=="":
    text="sorry i can't understand what you said" 
    speak(text)
else:
    text="that's what i found on google about it"
    speak(text)
    webbrowser.open("https://google.com/search?q="+a)

