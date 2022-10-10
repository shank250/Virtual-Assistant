import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
engine = pyttsx3.init()
r=sr.Recognizer()
def searchgoog(search):
    pywhatkit.search(search)
    
def whatsapp():
    pywhatkit.sendwahtmsg('+916391535319', 'Hello I am phyton',)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def listener():
    try:
        with sr.Microphone() as source:
            print("Yes I am listening...")
            r.adjust_for_ambient_noise(source)
            s = r.listen(source)
            print("Recognising")
            google_rec = r.recognize_google(s)
            return google_rec
    except:
        pass

def sent_word(your_sentence):
    fragmented = your_sentence.split()
def program_exit():
    exit()
def whatif():
    try:
        here = listener()
        print(here)
        fragmented = here.split()
        for i in fragmented:
            if i == "attendance" :
                speak("Hurry up Shashank! Its time for your school attendence.")
                break
            elif i == "assistant":
                speak("Hello! i'm Shashanks Assistant. How can i help you!")
                break
            elif i=="time":
                speak("If you are asking for time see it in clock. Don't ask to me.")
                break
            elif i == "name"  :
                speak("Hello! i'm Shashanks Assistant. How can i help you!")
                break
            elif i == "what's going on ?":
                speak("Just thinking...")
                break
            elif i == "present":
                speak("Shashank ! I have listened someone said Preseent sir in the class. May be the attendence is going on!")
                break
            elif i == "listen":
                speak("yes, what happened")
                x = listener()
                searchgoog(x)
            elif i == "WhatsApp":
                speak("What message you want to send")
                sender_name = "Sister"
                message_text = listener()
                print(message_text)
                tim = time.localtime()
                hour_time = tim.tm_hour
                min_time = tim.tm_min
                pywhatkit.sendwhatmsg('+916391535319', message_text, hour_time, min_time + 1)
                print("message sent")
            elif i == "stop":
                speak("Okay! Shashak")
                program_exit()
    except:
        pass
while True:
    whatif()
