import sys
import os
import androidhelper
import urllib.request as ur
from qsl4ahelper.fullscreenwrapper2 import *
import random
import time

try:
    import gdata.docs.service
except ImportError:
    gdata = None

# Initialize SL4A
droid = androidhelper.Android()
S2Tdroid = androidhelper.Android()

dtime = time.strftime

# Kairen : Virtual Assistant A.I bot
# Frontend : Python
# Backend  : QPython3L


def Kairen():

    print("0. Shutdown Kairen")
    print("1. Introduction")
    print("2. Tell me the date")
    print("3. Tell me the time")
    print("4. Tell me the month")
    print("5. Tell me the year")
    print("6. Tell me the day")
    print("7. Vibration mode")
    print("8. Testing python on Android")
    print("9. Generating a password")
    print("10. Speech Recognizer (Speech to Text)")
    print("11. Speech Recognizer (Speech to Speech)")

    droid.ttsSpeak("Hello Ma'am")
    droid.ttsSpeak("I am Kairen")
    droid.ttsSpeak("Nice to meet you")
    droid.ttsSpeak("How can I help you")
    droid.makeToast("Hello Ma'am 😊 \nI am Kairen \nNice to meet you 😊")
    droid.makeToast("How can I help you")

    # ---------------- FUNCTIONS ---------------- #

    def Help():
        droid.ttsSpeak("Do you want to know something else Ma'am")
        droid.makeToast("Do you want to know something else Ma'am 👩‍💼")

        Help_choice = str(input("Do you want to know something else (Y/N) : "))

        if Help_choice in ['Y', 'y']:
            loopwork()
        elif Help_choice in ['N', 'n']:
            greet()
        else:
            droid.ttsSpeak("Please Enter A Valid Choice Ma'am")
            droid.makeToast("Please Enter a valid choice Ma'am 👩‍💼")
            loopwork()

    def introduction():
        msg = [
            "Nice to meet you Ma'am",
            "My name is Kairen",
            "I am an A.I. version 1.0.0 designed by Varun on 21st December 2021",
            "I am your new personal assistant",
            "I am still an early access chatbot type A.I.",
            "So I can only do a few tasks",
            "How can I help you"
        ]
        for line in msg:
            print(line)
            droid.ttsSpeak(line)

    def date():
        result = dtime("%d %B, %Y")
        droid.ttsSpeak(result)
        droid.makeToast(result)

    def time_now():
        result = dtime("%I:%M %p")
        droid.ttsSpeak(result)
        droid.makeToast(result)

    def month():
        result = dtime("%B")
        droid.ttsSpeak(result)
        droid.makeToast(result)

    def year():
        result = dtime("%Y")
        droid.ttsSpeak(result)
        droid.makeToast(result)

    def day():
        result = dtime("Today is %A")
        droid.ttsSpeak(result)
        droid.makeToast(result)

    def greet():
        droid.ttsSpeak("Thank you")
        droid.ttsSpeak("Have a nice day Ma'am")
        droid.makeToast("Thank you 😊 \n Have a nice day Ma'am 😊")

    def vibration():
        droid.ttsSpeak("Vibration mode activated")
        droid.makeToast("Vibration Mode Activated 📱")
        droid.vibrate(2000)

    def Speak_to_Text():
        result = S2Tdroid.recognizeSpeech("Speak")
        return result.result  # Fixed: .result instead of [1]

    def Speak_to_Speak():
        text = Speak_to_Text()
        if text:
            droid.ttsSpeak(text)
            droid.makeToast(text)

    def password_generator():
        UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        LC = "abcdefghijklmnopqrstuvwxyz"
        SC = "-_@&$€()<>*/:;#%=![]{}√¢£¥©®^Δ§¦"
        NC = "1234567890"

        Use_for = UC + LC + SC + NC
        length_for_password = 8

        password = "".join(random.sample(Use_for, length_for_password))
        print("Your password is generated:", password)
        droid.ttsSpeak("Your password is generated")
        droid.makeToast(password)

    # ---------------- MAIN LOOP ---------------- #

    def loopwork():
        try:
            choice = int(input("Enter the choice: "))
        except ValueError:
            droid.ttsSpeak("Please enter a valid number")
            return loopwork()

        if choice == 0:
            greet()
            sys.exit(0)
        elif choice == 1:
            introduction()
            Help()
        elif choice == 2:
            date()
            Help()
        elif choice == 3:
            time_now()
            Help()
        elif choice == 4:
            month()
            Help()
        elif choice == 5:
            year()
            Help()
        elif choice == 6:
            day()
            Help()
        elif choice == 7:
            vibration()
            Help()
        elif choice == 8:
            droid.ttsSpeak("Python Testing module not fully implemented yet")
            droid.makeToast("Testing feature is in development")
            Help()
        elif choice == 9:
            password_generator()
            Help()
        elif choice == 10:
            text = Speak_to_Text()
            print("You said:", text)
            droid.makeToast(text or "No speech detected")
            Help()
        elif choice == 11:
            Speak_to_Speak()
            Help()
        else:
            greet()

    # Start
    loopwork()


Kairen()
