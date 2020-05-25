from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/v1/leds-on')
def turn_on_leds():
    response = jsonify (
        message = "Leds are turned on"
    )
    return response

@app.route('/api/v1/leds-off')
def turn_off_leds():
    return 'Leds are turned off'

@app.route('/api/v1/relay-all-on')
def turn_on_relay():
    return 'Relay turned on'

@app.route('/api/v1/relay-all-off')
def turn_off_relay():
    return 'Relay turned off'

if __name__ == "__main__":
    app.run('0.0.0.0', 8080)