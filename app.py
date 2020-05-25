from flask import Flask
from flask import jsonify
from Leds import Leds
from Relay import Relay
from subprocess import call
import subprocess
import os
import signal
from Voice import Voice
from ProcessUtil import ProcessUtil

app = Flask(__name__)

processUtil = ProcessUtil()

voice_process_id = -1
proc = None

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/v1/self-test')
def self_test():
    processUtil.self_test()
    response = jsonify (
        message = "Self test in progress"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/relays-state')
def relay_state():
    state = processUtil.switches_state();
    response = jsonify (
        state = state
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/heater-on')
def heater_on():
    processUtil.switch_on(1)
    response = jsonify(
        message = "Heater is on"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response;

@app.route('/api/v1/heater-off')
def heater_off():
    processUtil.switch_off(1)
    response = jsonify(
        message = "Heater is off"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/light-on')
def light_on():
    processUtil.switch_on(0)
    response = jsonify(
        message = "Light is on"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/light-off')
def light_off():
    processUtil.switch_off(0)
    response = jsonify(
        message = "Light is off"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/leds-on')
def turn_on_leds():
    processUtil.leds_on()
    response = jsonify (
        message = "Leds are turned on"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/leds-off')
def turn_off_leds():
    processUtil.leds_off()
    response = jsonify (
        message = "Leds are turned off"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/relay-all-on')
def turn_on_relay():
    processUtil.relay_on()
    response = jsonify(
        message = "Relay all switches on"    
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/relay-all-off')
def turn_off_relay():
    processUtil.relay_off()
    response = jsonify(
        message = "Relay all swiches off"
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response    

@app.route('/api/v1/mic-on')
def start_voice():
    global proc
    processUtil.mic_on()
    global voice_process_id
    strMessage = ""
    if (voice_process_id == -1):
        #process = subprocess.Popen(["python3", "VoiceApp.py"])
        proc = subprocess.Popen(["python3", "VoiceApp.py"])
        voice_process_id = proc.pid
        strMessage = "Voice process started!"
    else:
        strMessage = "Voice process has already started on Process Id: " + str(voice_process_id) 
    
    response = jsonify (
        message = strMessage
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/mic-off')
def stop_voice():
    global proc
    global voice_process_id
    strMessage = ""
    if voice_process_id == -1:
        strMessage = "Cannot stop what has not started"
    else:
        proc.terminate()
        proc.kill()
        voice_process_id = -1
        strMessage = "Process killed and voice proc id reset"
        
    response = jsonify(
        message = strMessage
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run('0.0.0.0', 8080, False, False)