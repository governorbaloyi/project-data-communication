from subprocess import call
import speech_recognition as sr
import serial
from time import sleep
from Leds import Leds
from Relay import Relay
from ProcessUtil import ProcessUtil

processUtil = ProcessUtil()

class Voice():
    def __init__(self):
        self.r = sr.Recognizer()
        
    def listen1(self):
        with sr.Microphone(device_index = 2) as source:
            self.r.adjust_for_ambient_noise(source)
            print("Say something");
            audio = self.r.listen(source)
            print("got it")
        return audio
    
    def voice(self, audio1):
        try:
            text1 = self.r.recognize_google(audio1)
            ## call('espeak ' + text, shell=True)
            print("You said: " + text1);
            return text1;
        except sr.UnknownValueError:
            self.say_text("I could not understand")
            print("I could not understand")
            return 0
        except sr.RequestError as e:
            print("Could not request results from Google")
            return 0
        
    @staticmethod
    def say_text(text):
        call(["espeak", "-s140 -ven+18 -z", " " + text])
        
    def on(self):
        audio1 = self.listen1()
        text = self.voice(audio1);
        print(text)
        try:
            if 'light on' in text:
                self.say_text("Okay Sir, Prepare for brightness")
                processUtil.switch_on(0)
                print("Lights on");
            elif 'light off' in text:
                self.say_text("Okay Sir, Prepare for less brightness")
                processUtil.switch_off(0)
                print("Lights off")
            elif 'heater on' in text:
                self.say_text("Okay Sir, Warming up the room")
                processUtil.switch_on(1)
            elif 'heater off' in text:
                self.say_text("Okay Sir, Cooling down the room")
                processUtil.switch_off(1)
        except:
            print("Unknown Exception")
        
    def activate(self):
        
        active = True
        
        while(active):
            audio1 = self.listen1()
            text = self.voice(audio1)
            if text == 'hello':
                self.say_text("Okay master, waiting for your command")
                self.on()
            elif text == 'close':
                self.say_text("Thank you, bye")
                active = False
            else:
                self.say_text("Please repeat")
                
        print("Voice closed...")
        
    
        
