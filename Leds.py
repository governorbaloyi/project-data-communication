import RPi.GPIO as GPIO

class Leds():
    def __init__(self, *args):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pins = args
        self.set_mode_out_all()
        self.all_off()
    
    def set_mode_out(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        
    def set_mode_out_all(self):
        for pin in self.pins:
            self.set_mode_out(pin)
        
    def output_high(self, pin):
        GPIO.output(pin, GPIO.HIGH)
        
    def all_off(self):
        for pin in self.pins:
            self.off(pin)
    
    def output_low(Self, pin):
        GPIO.output(pin, GPIO.LOW)
    
    def all_on(self):
        for pin in self.pins:
            self.on(pin)
    
    def off(self, pin):
        self.output_low(pin)
         
    def on(self, pin):
        self.output_high(pin)
    
    def cleanup(self):
        GPIO.cleanup()
        
    def __del__(self):
        self.cleanup()
        
    
        