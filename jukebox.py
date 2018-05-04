import json
import vlc
from flask import Flask
from flask import jsonify
app = Flask(__name__)

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()
state = {'current': 'Not Playing'}

with open('stations.json', 'r') as f:
    stations = json.load(f)

@app.route('/station')
def list_of_stations():
    return jsonify(stations)

@app.route('/station/<name>')
def change_station(name):
    media=instance.media_new(stations[name]["url"])
    player.set_media(media)
    print(f'Switching to: {stations[name]["url"]}')
    player.play()
    state['current'] = name
    return(f'{state["current"]}')

@app.route('/state')
def health():
    return(f'{state["current"]}')

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

