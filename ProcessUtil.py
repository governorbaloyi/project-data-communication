from Leds import Leds
from Relay import Relay
from time import sleep

RELAY = [18, 23, 24, 25]
LEDS = [4, 17, 27, 22, 5, 6, 13, 19, 26]

class ProcessUtil():
    def __init__(self):
        self.leds = Leds(4, 17, 27, 22, 5, 6, 13, 19, 26)
        self.relay = Relay(18, 23, 24, 25)
        
    def self_test(self):
        for i in range(4):
            sleep(1)
            self.switch_on(i)
        
        for i in range(4):
            sleep(1)
            self.switch_off(i)
    
    def switch_on(self, index):
        i = self.relay.on(RELAY[index])
        self.leds.off(i[0])
        self.leds.on(i[1])
    
    def switch_off(self, index):
        i = self.relay.off(RELAY[index])
        self.leds.on(i[0])
        self.leds.off(i[1])
        
    def leds_on(self):
        self.leds.all_on()
        
    def leds_off(self):
        self.leds.all_off()
    
    def led_on(self, index):
        self.leds.on(LEDS[index])
        
    def led_off(self, index):
        self.leds.off(LEDS[index])
        
    def relay_on(self):
        self.relay.all_on()
        
    def relay_off(self):
        self.relay_all_off()