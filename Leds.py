from gpiozero import LEDBoard

class Leds():
    def __init__(self, *args):
        self.leds = LEDBoard(*args)
        
    def on(self):
        self.leds.on()
        
    def off(self):
        self.leds.off()
        
    
        