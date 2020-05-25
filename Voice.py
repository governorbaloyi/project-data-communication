from subprocess import call
import speech_recognition as sr
import serial
from time import sleep
from Leds import Leds
from Relay import Relay

r = sr.Recognizer()
leds = Leds(4, 17, 27, 22, 5, 6, 13, 19, 26)

R1 = 18
R2 = 23
R3 = 24
R4 = 25

relay = Relay(18, 23, 24, 25)

def listen1():
    with sr.Microphone(device_index = 2) as source:
        r.adjust_for_ambient_noise(source)
        print("Say something");
        audio = r.listen(source)
        print("got it")
    return audio

def voice(audio1):
    try:
        text1 = r.recognize_google(audio1)
##        call('espeak ' + text, shell=True)
        print("You said: " + text1);
        return text1;
    except sr.UnknownValueError:
        call(["espeak", "-s140 -ven+18 -z", "Google Speech Recognition could not understand"])
        print("Google Speech Recognition could not understand")
        return 0
    except sr.RequestError as e:
        print("Could not request results from Google")
        return 0

def main():
    audio1 = listen1()
    text = voice(audio1);
    
    print(text)
    
    if 'light on' in text:
        call(["espeak", "-s140 -ven+18 -z", " Okay Sir, Switching ON the Lights"])
        leds.on()
        relay.on()
        print("Lights on");
    elif 'light off' in text:
        call(["espeak", "-s140 -ven+18 -z", " Okay Sir, Switching off the Lights"])
        leds.off()
        print("Lights off")
    text = {}

if __name__ == "__main__":
    while(True):
        audio1 = listen1()
        text = voice(audio1)
        if text == 'hello':
            text = {}
            call(["espeak", "-s140 -ven+18 -z", " Okay master, waiting for your command"])
            main()
        else:
            call(["espeak", "-s140 -ven+18 -z", " Please repeat"])

