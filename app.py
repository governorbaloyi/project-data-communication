from flask import Flask
from flask import jsonify
from Leds import Leds
from Relay import Relay
from subprocess import call
import subprocess
import os
import signal

app = Flask(__name__)

leds = Leds(4, 17, 27, 22, 5, 6, 13, 19, 26)
relay = Relay(18, 23, 24, 25)

voice_process_id = -1

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/v1/leds-on')
def turn_on_leds():
    leds.on()
    response = jsonify (
        message = "Leds are turned on"
    )
    return response

@app.route('/api/v1/leds-off')
def turn_off_leds():
    leds.off()
    response = jsonify (
        message = "Leds are turned off"
    )
    return response

@app.route('/api/v1/relay-all-on')
def turn_on_relay():
    relay.all_on()
    response = jsonify(
        message = "Relay all switches on"    
    )
    return response

@app.route('/api/v1/relay-all-off')
def turn_off_relay():
    relay.all_off()
    response = jsonify(
        message = "Relay all swiches off"
    )
    return response    

@app.route('/api/v1/mic-on')
def start_voice():
    global voice_process_id
    strMessage = ""
    if (voice_process_id == -1):
        process = subprocess.Popen(["python3", "Voice.py"])
        voice_process_id = process.pid
        strMessage = "Voice process started!"
    else:
        strMessage = "Voice process has already started on Process Id: " + str(voice_process_id) 
    
    response = jsonify (
        message = strMessage
    )
    
    return response

@app.route('/api/v1/mic-off')
def stop_voice():
    global voice_process_id
    strMessage = ""
    if voice_process_id == -1:
        strMessage = "Cannot stop what has not started"

    response = jsonify(
        message = strMessage
    )
    
    return response

if __name__ == "__main__":
    app.run('0.0.0.0', 8080, False, False)