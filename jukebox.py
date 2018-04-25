import json
import vlc
from flask import Flask
app = Flask(__name__)

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()
state = {'current': 'Not Playing'}

with open('stations.json', 'r') as f:
    stations = json.load(f)

@app.route('/')
def index():
    return """You can call the following endpoints:
/station for a list of available stations
/station/<station_name> to play a station
/state for the currently playing station
/control/stop to stop
/control/pause to stop the station but allow resuming via /start
/control/start to resume playback of the station
"""

@app.route('/station')
def list_of_stations():
    return(f'Available Stations: {", ".join(stations)} \n')

@app.route('/station/<name>')
def change_station(name):
    media=instance.media_new(stations[name]["url"])
    player.set_media(media)
    print(f'Switching to: {stations[name]["url"]}')
    player.play()
    state['current'] = 'Playing: ' + stations[name]["friendly_name"]
    return(f'{state["current"]}\n')

@app.route('/state')
def health():
    return(f'{state["current"]}\n')

@app.route('/control/<status>')
def control(status):
    if status == 'stop':
        player.stop()
        state['current'] = 'Not Playing'
        return('Stopping Music\n')
    if status == 'pause':
        player.stop()
        return('Pausing Music\n')
    if status == 'play':
        if state['current'] == 'Not Playing':
            return('Nothing to play, try calling /station\n')
        else:
            player.play()
            return(f'{state["current"]}\n')
    else:
        return('You can only call: stop, play or pause\n')
