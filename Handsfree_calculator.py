import speech_recognition as sr
import playsound
import gtts as gTTS
import pyttsx3
import time

r1=sr.Recognizer()
engine=pyttsx3.init()

print("Welcome to voice controlled calculator!")
engine.say("Welcome to voice controlled calculator")
engine.runAndWait()

print("Do You want to run the calculator? Say yes or no!")
engine.say("Do You want to run the calculator?")
engine.runAndWait()
time.sleep(1)
engine.say("Say Yes Or No!")
engine.runAndWait()

global yon
global yon_text

with sr.Microphone() as source:
    print("Speak")
    yon=r1.listen(source,timeout=1,phrase_time_limit=20)

print("pass")

yon_text=r1.recognize_google(yon)

print(yon_text)

def calc():
    with sr.Microphone() as source:
        print("------------------------------------------------------------------")
        print("You have to just say the expression you want to calculate")
        engine.say("You have to just say the expression you want to calculate")
        engine.runAndWait()
        engine.say("Now Speak")
        print("\nNow Speak!")
        engine.runAndWait()
        audio=r1.listen(source,timeout=1,phrase_time_limit=10)

    print("pass")


    text=r1.recognize_google(audio)
    print(text)

    list1=text.split()
    length=len(list1)
    first_value=int(list1[0])
    second_value=int(list1[length-1])

    iserror=False

    ans=0

    if "+" in list1:
        ans=first_value+second_value
    elif "plus" in list1:
        ans=first_value+second_value
    elif "added" in list1:
        ans=ans=first_value+second_value
    elif "-" in list1:
        ans=first_value-second_value
    elif "minus" in list1:
        ans=first_value-second_value
    elif "subtracted" in list1:
        ans=second_value-first_value       
    elif "x" in list1:
        ans=first_value*second_value
    elif "X" in list1:
        ans=first_value*second_value
    elif "multiplied" in list1:
        ans=first_value*second_value
    elif "mutiply" in list1:
        ans=first_value*second_value
    elif "/" in list1:
        ans=first_value/second_value
    elif "divided" in list1:
        ans=first_value/second_value
    elif "divide" in list1:
        ans=first_value/second_value
    else:
        iserror=True
        ans=""
        print("error in understanding")
        engine.say("Sorry! couldn't hear that")
        engine.runAndWait()

    print(ans)

    if iserror==True:
        return
    else:
        engine.say("Your Answer is ")
        engine.runAndWait()
        engine.say(ans)
        engine.runAndWait()
        return


def choice():

    global yon
    global yon_text
    if yon_text=="yes" or yon_text=="Yes" or "yes" in yon_text:
        calc()
        print("Do You Want To Use Calculator Again? Say Yes or No")
        engine.say("Do You Want To Use Calculator Again?")
        engine.runAndWait()
        time.sleep(1)
        engine.say("Say Yes Or No!")
        engine.runAndWait()
        with sr.Microphone() as source:
            yon=r1.listen(source,timeout=1,phrase_time_limit=10)
        print("Pass")
        
        yon_text=r1.recognize_google(yon)

        print(yon_text)

        choice()
            

        


    else:
        print("Exiting From Calculator")
        engine.say("Exiting From Calculator")
        engine.runAndWait()
        print("\n-------------------Thank You------------------")
        engine.say("Thank You!")
        engine.runAndWait()
        return

choice()

delay=input("Press any key to exit:")

